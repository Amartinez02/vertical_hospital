from odoo import http
from odoo.http import request, Response

import json
import logging
import werkzeug

class Qspatients(http.Controller):

    @http.route('/api/<path:subpath>/<sequence>', type='http', cors='*', csrf=False, auth="public", methods=["GET"])
    def patients(self, subpath, sequence, **kwargs):
        
        desired_path = request.env['ir.config_parameter'].sudo().search([('key', '=', 'vertical.hospital.api.rest')])
        logging.error('*****PATH patients****')
        logging.error(subpath)
        logging.error(desired_path.value)

        if subpath == desired_path.value:
            record = request.env['qs.patients'].sudo().search([('name', '=', sequence)])
            data = None

            if record:
                data = {
                    "seq": record.name,
                    "name": record.full_name, 
                    "dni": record.dni, 
                    "state": record.state
                }
            else:
                data = {
                    "message" : "No records"
                }
        
            return Response(json.dumps(data), content_type='application/json;charset=utf-8', status=200)

        raise werkzeug.exceptions.NotFound()