from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class QsApiRestSetting(models.TransientModel):
    _inherit = 'res.config.settings'
    
    api_path = fields.Char(string="Nombre API", config_parameter='vertical.hospital.api.rest')