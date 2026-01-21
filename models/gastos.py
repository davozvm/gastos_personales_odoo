from odoo import models, fields, api
from datetime import date


class GastoPersonal(models.Model):
    _name = 'gasto.personal'
    _description = 'Gasto Personal'

    name = fields.Char(string="Descripción", required=True)
    monto = fields.Float(string="Monto", required=True)
    fecha = fields.Date(string="Fecha", default=date.today)

    categoria = fields.Selection([
        ('comida', 'Comida'),
        ('transporte', 'Transporte'),
        ('hogar', 'Hogar'),
        ('ocio', 'Ocio'),
        ('otros', 'Otros'),
    ], string="Categoría", required=True)

    estado = fields.Selection([
        ('draft', 'Borrador'),
        ('aprobado', 'Aprobado'),
    ], default='draft')

    def action_aprobar(self):
        self.estado = 'aprobado'