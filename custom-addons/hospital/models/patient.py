from odoo import api, fields, models

class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _description = "Patient Details"

    name=fields.Char(string="name", required=True)
    age=fields.Integer(string="age", required=True)
    is_child=fields.Boolean(string="is child?")
    gender=fields.Selection([
                             ('male', 'Male'),
                             ('female', 'Female'),
                             ('other', 'Other')
    ], string="gender", required=True)
    notes=fields.Text(string="Notes")
