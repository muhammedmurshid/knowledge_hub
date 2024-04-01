from odoo import models, fields, api, _


class KnowledgeForm(models.Model):
    _name = 'knowledge.form'
    _description = 'Knowledge Form'
    _rec_name = 'display_name'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    department_id = fields.Many2one('hr.department', string="Department", required=1)
    knowledge = fields.Html(string="Knowledge")

    def _compute_display_name(self):
        for record in self:
            if record.department_id:
                record.display_name = record.department_id.name + ' - ' + 'Knowledge'
