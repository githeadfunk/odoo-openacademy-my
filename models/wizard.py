import logging
from odoo import models, fields, api

_logger = logging.getLogger(__name__)

class Wizard(models.TransientModel):
    _name = 'openacademy.wizard'
    _description = "Wizard: Quick Registration of Attendees to Sessions"

    def _default_sessions(self):
        # _logger.debug('set default sessions', self)
        return self.env['openacademy.session'].browse(self._context.get('active_ids'))

    session_ids = fields.Many2one('openacademy.session', string="Sessions", 
        required=True, default=_default_sessions)
    attendee_ids = fields.Many2many('res.partner', string="Attendees")

    @api.multi
    def subscribe(self):
        for session in self.session_ids:
            session.attendee_ids |= self.attendee_ids
        return {}