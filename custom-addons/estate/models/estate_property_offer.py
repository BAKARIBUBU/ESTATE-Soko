# models/estate_property_offer.py
from odoo import models, fields

class EstatePropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "Property Offer"
    _order = "price desc"

    price = fields.Float()
    status = fields.Selection([
        ('accepted', 'Accepted'),
        ('refused', 'Refused')
        ],
       copy=False
      )
    partner_id = fields.Many2one('res.partner', required=True, string='Partner')

    # Many2one Relation to Property
    property_id = fields.Many2one(
        'estate.property',
        string='Property',
        required=True,
        ondelete='cascade'
    )