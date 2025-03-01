==================================
Sale Order Qty change no recompute
==================================

.. 
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   !! This file is generated by oca-gen-addon-readme !!
   !! changes will be overwritten.                   !!
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   !! source digest: sha256:28ba7eb73f86e6234cbb801dfd2a2759a7f75855b5e3c894ff058771020e9315
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

.. |badge1| image:: https://img.shields.io/badge/maturity-Beta-yellow.png
    :target: https://odoo-community.org/page/development-status
    :alt: Beta
.. |badge2| image:: https://img.shields.io/badge/licence-AGPL--3-blue.png
    :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
    :alt: License: AGPL-3
.. |badge3| image:: https://img.shields.io/badge/github-OCA%2Fsale--workflow-lightgray.png?logo=github
    :target: https://github.com/OCA/sale-workflow/tree/17.0/sale_order_qty_change_no_recompute
    :alt: OCA/sale-workflow
.. |badge4| image:: https://img.shields.io/badge/weblate-Translate%20me-F47D42.png
    :target: https://translation.odoo-community.org/projects/sale-workflow-17-0/sale-workflow-17-0-sale_order_qty_change_no_recompute
    :alt: Translate me on Weblate
.. |badge5| image:: https://img.shields.io/badge/runboat-Try%20me-875A7B.png
    :target: https://runboat.odoo-community.org/builds?repo=OCA/sale-workflow&target_branch=17.0
    :alt: Try me on Runboat

|badge1| |badge2| |badge3| |badge4| |badge5|

A lot of business don't set different prices according the quantity of
the product to sell, and they see very annoying to set a manual price
after the negotiation with the customer, and see it changed when they
vary the demanded quantity.

This module prevents this avoiding the recomputation of the price unit,
discount and pricelist item fields if only the quantity has been changed
in the sales order line.

**Table of contents**

.. contents::
   :local:

Usage
=====

To use this module, you need to:

1. Create a new sale order.
2. Add product line and set custom unit price.
3. Save sale order.
4. Edit sale order and change quantity (custom unit price not been
   reset).

Known issues / Roadmap
======================

-  Having this module installed may alter test results of other modules
   expecting to have the price fields recomputed when changing
   quantities.

Bug Tracker
===========

Bugs are tracked on `GitHub Issues <https://github.com/OCA/sale-workflow/issues>`_.
In case of trouble, please check there if your issue has already been reported.
If you spotted it first, help us to smash it by providing a detailed and welcomed
`feedback <https://github.com/OCA/sale-workflow/issues/new?body=module:%20sale_order_qty_change_no_recompute%0Aversion:%2017.0%0A%0A**Steps%20to%20reproduce**%0A-%20...%0A%0A**Current%20behavior**%0A%0A**Expected%20behavior**>`_.

Do not contact contributors directly about support or help with technical issues.

Credits
=======

Authors
-------

* Tecnativa

Contributors
------------

-  `Tecnativa <https://www.tecnativa.com>`__:

   -  Víctor Martínez
   -  Pedro M. Baeza
   -  César A. Sánchez

Maintainers
-----------

This module is maintained by the OCA.

.. image:: https://odoo-community.org/logo.png
   :alt: Odoo Community Association
   :target: https://odoo-community.org

OCA, or the Odoo Community Association, is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.

.. |maintainer-victoralmau| image:: https://github.com/victoralmau.png?size=40px
    :target: https://github.com/victoralmau
    :alt: victoralmau

Current `maintainer <https://odoo-community.org/page/maintainer-role>`__:

|maintainer-victoralmau| 

This module is part of the `OCA/sale-workflow <https://github.com/OCA/sale-workflow/tree/17.0/sale_order_qty_change_no_recompute>`_ project on GitHub.

You are welcome to contribute. To learn how please visit https://odoo-community.org/page/Contribute.
