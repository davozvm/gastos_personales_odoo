from odoo import models, fields, api
from datetime import date

class GastoPersonal(models.Model):
    _name = 'gasto.personal'
    _description = 'Gasto Personal'

    name = fields.Char(string="Descripción", required=True)
    monto = fields.Float(string="Monto", required=True)
    
    fecha = fields.Date(string="Fecha", default=lambda self: date.today())

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
    ], string="Estado", default='draft', readonly=True)

    def action_aprobar(self):
        for record in self:
            record.estado = 'aprobado'