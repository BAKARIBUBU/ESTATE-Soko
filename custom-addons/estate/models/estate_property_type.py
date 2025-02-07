from odoo import models, api, fields

class EstatePropertyType(models.Model):
    _name = 'estate.property.type'
    _description = 'Real Estate Property Type'

    name = fields.Char(required=True)
    
    # Inverse relation to property
    property_ids = fields.One2many(
        'estate.property',
        'property_type_id',
        string='Properties')

