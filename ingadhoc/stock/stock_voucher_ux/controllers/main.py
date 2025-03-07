# Copyright 2017 ACSONE SA/NV
# Copyright 2018 - Brain-tec AG - Carlos Jesus Cebrian
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)
import io
import json
import urllib.parse
import re

from odoo.http import route, request
from odoo.addons.web.controllers import report
from PyPDF2 import PdfFileReader


class ReportController(report.ReportController):

    @route()
    def report_download(self, data, context=None):
        """This function is used by 'qwebactionmanager.js' in order to trigger
        the download of a py3o/controller report.
        :param data: a javascript array JSON.stringified containg report
        internal url ([0]) and type [1]
        :returns: Response with a filetoken cookie and an attachment header
        """
        response = super().report_download(data, context)
        #NTH detect if the binary is a PDF, no matter ifn it was generated by a QWeb or Aeroo
        requestcontent = json.loads(data)
        url, type = requestcontent[0], requestcontent[1]
        # context_part = json.loads(data)[0].split('context=')[1]
        # context_dict = json.loads(urllib.parse.unquote(context_part))
        # model = context_dict.get('params', {}).get('model')
        if type == 'aeroo':
            context_part = json.loads(data)[0].split('context=')[1]
            context_dict = json.loads(urllib.parse.unquote(context_part))
            model = context_dict.get('params', {}).get('model')
            if model == 'stock.picking':
                context_part = json.loads(data)[0].split('context=')[1]
                context_dict = json.loads(urllib.parse.unquote(context_part))
                picking_id  = context_dict.get('active_ids')
                # Get assign on the context. If true, then is not an autoprinted
                assign  = context_dict.get('assign')
                book_id = request.env['stock.picking'].browse(picking_id).book_id
                if assign and book_id:
                    if picking_id:
                        pdf_response = response.response[0]
                        reader = PdfFileReader(io.BytesIO(pdf_response))
                        # The number of pages will assign the number of vouchers
                        number_pages = reader.getNumPages()

                    # See if there are vouchers already assigned. If not, then it assigns the vouchers
                    if not request.env['stock.picking'].browse(picking_id).voucher_ids and book_id:
                        request.env['stock.picking'].browse(picking_id).assign_numbers(number_pages, book_id)
        else:
            dict_context = json.loads(context)
            model = dict_context['active_model']
            if model == 'stock.picking':
            # If the report is not an aeroo, the assign method should only assign one voucher
                match = re.search(r'(\d+)$', json.loads(data)[0])
                if match:
                    picking_id = int(match.group(1))
                    book_id = request.env['stock.picking'].browse(picking_id).book_id
                    if not request.env['stock.picking'].browse(picking_id).voucher_ids and book_id:
                        request.env['stock.picking'].browse(picking_id).assign_numbers(1, book_id)

        return response
