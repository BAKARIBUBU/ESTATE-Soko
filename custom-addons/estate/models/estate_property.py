from odoo import api,fields, models
from dateutil.relativedelta import relativedelta

class EstateProperty(models.Model):
    _name="estate.property"
    _description = "Estate Property"
    _rec_name = "name"

    active = fields.Boolean(
        string="Active",
        default=True,
        help="If unchecked, this property will be hidden"
    )

    state = fields.Selection(
        [
            ('new', 'New'),
            ('offer_received', 'Offer Received'),
            ('offer_accepted', 'Offer Accepted'),
            ('sold', 'Sold'),
            ('cancelled', 'Cancelled')
        ],
        string="Status",
        required=True,
        copy=False,
        default='new'
    )


    name=fields.Char(string="name",default="Unknown",required=True)
    description=fields.Text(string="description",required=True)
    postcode=fields.Char(string="postcode",required=True)
    date_availability=fields.Date(string="date",copy=False,
                                  default=lambda self: fields.Date.today() + relativedelta(months=3),
                                  required=True)
    expected_price=fields.Float(string="expected price",required=True)
    selling_price=fields.Float(string="selling price",readonly=True,copy=False, required=True)
    bedrooms=fields.Integer(string="bedrooms",default=2,required=True)
    living_area=fields.Integer(string="living area",required=True)
    facades=fields.Integer(string="facades",required=True)
    garage=fields.Boolean(string="garage",required=True)
    garden_area=fields.Integer(string="garden area",required=True)
    garden_orientation = fields.Selection([('north', 'North'),
                                           ('south', 'South'),
                                           ('east', 'East'),
                                           ('west', 'West')
                                          ],
                                          string="Garden Orientation",
                                          required=True)
    buyer_id = fields.Many2one(
        'res.partner',
        string='Buyer',
        copy=False,
        help='Select a buyer'
    )
    salesperson_id = fields.Many2one(
        'res.users',
        string='Salesperson',
        default=lambda self: self.env.user,
        required=True,
        help='Select a salesperson'

    )

    # Many2one Relationship to Property Type
    property_type_id = fields.Many2one(
        'estate.property.type',
        string='Property Type',
        help="Select a property type",)

    # Many2many Relation to Property Tags
    tag_ids = fields.Many2many(
        'estate.property.tag',
        string='Tags',
        help='Property Tags'
    )
    # One2many Relation to Property Offers
    offer_ids = fields.One2many(
        'estate.property.offer',
        'property_id',
        string='Offers'
    )

