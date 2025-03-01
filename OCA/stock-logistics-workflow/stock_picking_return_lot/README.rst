========================
Stock Picking Return Lot
========================

.. 
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   !! This file is generated by oca-gen-addon-readme !!
   !! changes will be overwritten.                   !!
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   !! source digest: sha256:0bfc4f4d34a78ccaf3796177eab802589526e93955d42980baff6a46743cec2d
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

.. |badge1| image:: https://img.shields.io/badge/maturity-Beta-yellow.png
    :target: https://odoo-community.org/page/development-status
    :alt: Beta
.. |badge2| image:: https://img.shields.io/badge/licence-AGPL--3-blue.png
    :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
    :alt: License: AGPL-3
.. |badge3| image:: https://img.shields.io/badge/github-OCA%2Fstock--logistics--workflow-lightgray.png?logo=github
    :target: https://github.com/OCA/stock-logistics-workflow/tree/17.0/stock_picking_return_lot
    :alt: OCA/stock-logistics-workflow
.. |badge4| image:: https://img.shields.io/badge/weblate-Translate%20me-F47D42.png
    :target: https://translation.odoo-community.org/projects/stock-logistics-workflow-17-0/stock-logistics-workflow-17-0-stock_picking_return_lot
    :alt: Translate me on Weblate
.. |badge5| image:: https://img.shields.io/badge/runboat-Try%20me-875A7B.png
    :target: https://runboat.odoo-community.org/builds?repo=OCA/stock-logistics-workflow&target_branch=17.0
    :alt: Try me on Runboat

|badge1| |badge2| |badge3| |badge4| |badge5|

When a product is tracked by lot or serial number and is returned by a
customer, it’s crucial to clearly indicate to the user which lot or
serial number can be accepted. This way, we prevent user from receiving
a product with a lot or serial number different from the original
delivery.

This module enhances the return process by creating a separate return
line for each product/lot and automatically pre-filling it with the lot
from the original delivery. It relies on the `Stock Restrict
Lot <https://github.com/OCA/stock-logistics-workflow/tree/16.0/stock_restrict_lot>`__
module to enforce accurate tracking, ensuring that the reception order
reflects the correct lot or serial number that should be received.

**Table of contents**

.. contents::
   :local:

Bug Tracker
===========

Bugs are tracked on `GitHub Issues <https://github.com/OCA/stock-logistics-workflow/issues>`_.
In case of trouble, please check there if your issue has already been reported.
If you spotted it first, help us to smash it by providing a detailed and welcomed
`feedback <https://github.com/OCA/stock-logistics-workflow/issues/new?body=module:%20stock_picking_return_lot%0Aversion:%2017.0%0A%0A**Steps%20to%20reproduce**%0A-%20...%0A%0A**Current%20behavior**%0A%0A**Expected%20behavior**>`_.

Do not contact contributors directly about support or help with technical issues.

Credits
=======

Authors
-------

* Camptocamp
* ACSONE SA/NV

Contributors
------------

-  Iryna Vyshnevska <i.vyshnevska@mobilunity.com>
-  `PyTech SRL <https://www.pytech.it>`__:

   -  Alessio Renda
   -  Sebastiano Picchi

-  `Ooops404 <https://www.ooops404.com>`__:

   -  Foresti Francesco <francesco.foresti@ooops404.com>

-  `ACSONE SA/NV <https://www.acsone.eu>`__:

   -  Souheil Bejaoui <souheil.bejaoui@acsone.eu>

-  `APSL-Nagarro <https://apsl.tech>`__:

   -  Antoni Marroig <amarroig@apsl.net>

Maintainers
-----------

This module is maintained by the OCA.

.. image:: https://odoo-community.org/logo.png
   :alt: Odoo Community Association
   :target: https://odoo-community.org

OCA, or the Odoo Community Association, is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.

This module is part of the `OCA/stock-logistics-workflow <https://github.com/OCA/stock-logistics-workflow/tree/17.0/stock_picking_return_lot>`_ project on GitHub.

You are welcome to contribute. To learn how please visit https://odoo-community.org/page/Contribute.
