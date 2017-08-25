# -*- coding: utf-8 -*-

from odoo import api, fields, models


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    @api.multi
    def _default_agents(self):
        """
        Definir o agent padrão de cada linha apartir do cadastro do cliente 
        :return: 
        """
        agents = []
        if self.env.context.get('participante_id'):
            partner = self.env['sped.participante'].browse(
                self.env.context['participante_id'])
            for agent in partner.agents:
                agents.append({'agent': agent.id,
                               'commission': agent.commission.id})
        return [(0, 0, x) for x in agents]

    agents = fields.One2many(
        default=_default_agents,
    )
