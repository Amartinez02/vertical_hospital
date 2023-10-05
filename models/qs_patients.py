from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
import re

STATES = [('draft', 'Borrador'), ('discharged', 'Alta'), ('admitted', 'Baja')]

class QSPatients(models.Model):
    _name = 'qs.patients'
    _description = 'Patients'
    _order = 'name desc'
    _inherit = ['mail.thread']

    name = fields.Char(string=u'Reference', readonly=True)
    full_name = fields.Char(string=u'Nombre y apellido')
    dni = fields.Char(string=u'DNI', tracking=True)
    discharged_date = fields.Datetime(string='Fecha hora de alta', default=fields.Datetime.now)
    state = fields.Selection(STATES, string=u'Estado', default='draft', tracking=True)
    treatment_ids = fields.Many2many(
        string=u'Tratamientos',
        comodel_name='qs.treatments',
        relation='qs_treatments_qs_patients_rel',
        column1='treatment_id',
        column2='patients_id')
    
    
    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('qs.patients.sequence') or 'New'
        return super(QSPatients, self).create(vals)

    @api.constrains('dni')
    def _check_dni(self):
        for rec in self:
            if rec.dni and not rec.dni.isnumeric():
                raise ValidationError(_('DNI invalido, solo se permiten números.'))