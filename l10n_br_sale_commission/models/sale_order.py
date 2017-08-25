# -*- coding: utf-8 -*-
# © 2017 KMEE INFORMATICA LTDA (https://www.kmee.com.br)
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from odoo import api,fields, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.onchange('participante_id')
    def _default_agents(self):
        for record in self:
            agents = []
            if record.participante_id:
                for agent in record.participante_id.agents:
                    agents.append({
                        'agent': agent.id,
                        'commission': agent.commission.id}
                    )
            record.agents = agents

    agents = fields.One2many(
        string="Agents & commissions",
        comodel_name="sale.order.line.agent",
        inverse_name="sale_line",
        copy=True,
        # readonly=True,
        default=_default_agents,
    )

    commission_free = fields.Boolean(
        string="Livre de comissão",
        store=True, readonly=True
    )
