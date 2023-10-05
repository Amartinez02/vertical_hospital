from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class QSTreatments(models.Model):
    _name = 'qs.treatments'
    _description = 'QSTreatments'
    _order = 'name desc'

    name = fields.Char(string=u'Código de tratamiento')
    description = fields.Char(string=u'Nombre tratamiento')
    doctor = fields.Char(string=u'Médico tratante')

    @api.constrains('name')
    def _check_name(self):
        for rec in self:
            if '026' in rec.name:
                raise ValidationError(_('El código de tratamiento no debe poder contener la secuencia “026”.'))
