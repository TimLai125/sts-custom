# -*- coding: utf-8 -*-
# Copyright 2017-2018 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, api
from odoo.addons.product_yahoo_auction_sst.models.product_template import \
    ProductTemplate


@api.model
def create(self, vals):
    print("stock_ext_sst")
    return super(ProductTemplate, self).create(vals)


class ProductTemplateHookCreate(models.AbstractModel):
    _name = "product.template.hook.create"

    def _register_hook(self):
        ProductTemplate.create = create
        return super(ProductTemplateHookCreate, self)._register_hook()
