# purchase_issue_tracker/models/issue_tracker.py
from odoo import models, fields, api
from odoo.exceptions import UserError


class PurchaseIssueTracker(models.Model):
    _name = 'purchase.issue.tracker'
    _description = 'Purchase Issue Tracker'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    # Main Fields
    vendor_id = fields.Many2one('res.partner', string="Vendor", required=True, domain="[('supplier_rank', '>', 0)]")
    po_no = fields.Many2one('purchase.order', string="PO Number", required=True)
    vendor_bill_id = fields.Many2one('account.move', string="Vendor Bill", required=True,
                                     domain="[('move_type', '=', 'in_invoice')]")
    bill_date = fields.Date(string="Bill Date", related='vendor_bill_id.invoice_date', readonly=True)
    solution = fields.Text(string="Solution")

    # Updated line_ids field with correct relation
    line_ids = fields.One2many('purchase.issue.tracker.line', 'issue_tracker_id', string="Issue Product Lines")

    # Status Field
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirm', 'Confirmed'),
        ('closed', 'Closed')
    ], string="Status", default='draft', tracking=True)

    show_confirm_button = fields.Boolean(compute="_compute_button_visibility")
    show_close_button = fields.Boolean(compute="_compute_button_visibility")
    show_draft_button = fields.Boolean(compute="_compute_button_visibility")

    @api.depends('state')
    def _compute_button_visibility(self):
        """Controls visibility of buttons based on state."""
        for record in self:
            record.show_confirm_button = record.state == 'draft'
            record.show_close_button = record.state == 'confirm'
            record.show_draft_button = record.state == 'closed'

    @api.onchange('vendor_bill_id')
    def _onchange_vendor_bill_id(self):
        """Load items from the selected vendor bill."""
        if self.vendor_bill_id:
            self.line_ids = [(5, 0, 0)]
            lines = []
            for line in self.vendor_bill_id.invoice_line_ids:
                if line.product_id:
                    lines.append((0, 0, {
                        'product_id': line.product_id.id,
                        'quantity': line.quantity,
                        'reason_id': False,
                        'remarks': '',
                    }))
            self.line_ids = lines

    def action_confirm(self):
        """Set the state to confirm only if the current state is 'draft'."""
        if self.state != 'draft':
            raise UserError("You can only confirm records in the draft state.")
        self.state = 'confirm'

    def action_close(self):
        """Set the state to closed, ensuring solution is provided, only if state is 'confirm'."""
        if self.state != 'confirm':
            raise UserError("You can only close records that are in the confirmed state.")
        if not self.solution:
            raise UserError("Please provide a solution before closing.")
        self.state = 'closed'

    def action_draft(self):
        """Return the record to the draft state if it is closed."""
        if self.state != 'closed':
            raise UserError("You can only reset records to draft from the closed state.")
        self.state = 'draft'


class PurchaseIssueTrackerLine(models.Model):
    _name = 'purchase.issue.tracker.line'
    _description = 'Purchase Issue Tracker Line'

    # Correct field reference to link to the main model
    issue_tracker_id = fields.Many2one('purchase.issue.tracker', string="Issue Tracker", required=True,
                                       ondelete='cascade')
    product_id = fields.Many2one('product.product', string="Item", required=True,
                                 default=lambda self: self.env['product.product'].search([], limit=1).id)
    quantity = fields.Float(string="Quantity", required=True)
    reason_id = fields.Many2one('damage.reason', string="Reason")
    remarks = fields.Text(string="Remarks")


class DamageReason(models.Model):
    _name = 'damage.reason'
    _description = 'Damage Reason'

    name = fields.Char(string="Reason", required=True)
