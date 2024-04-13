from odoo.addons.portal.controllers.portal import CustomerPortal
from odoo.http import request
from odoo import http
from ..help_func import validate_access_token, SHIP_MANAGEMENT, DOCKING


class Home(CustomerPortal):
    def _prepare_home_portal_values(self, counters):
        rtn = super(Home, self)._prepare_home_portal_values(counters)
        rtn["material_paint_quotes_count"] = (
            request.env["ship.material.paint.quotes.request"].sudo().search_count([])
        )
        return rtn

    @http.route(["/"], type="http", auth="public", website=True)
    def ship_home_view(self, **kw):
        is_validate, supplier = validate_access_token(SHIP_MANAGEMENT)
        if is_validate:
            pages = [
                ("/material-paint-quotes", "Material Paint Quotes"),
                ("/job-supplier-quotes", "Job Supplier Quotes"),
            ]
            vals = {"pages": pages}
            return request.render("supplier_portal.portal_home", vals)
        else:
            vals = {"supplier": supplier}
            return request.render("supplier_portal.portal_request_access", vals)

    @http.route(["/docking"], type="http", auth="public", website=True)
    def docking_home_view(self, **kw):
        is_validate, supplier = validate_access_token(DOCKING)
        if is_validate:
            pages = [
                ("/docking/docking-plans", "Docking Plans"),
                ("/docking/job-supplier-quotes", "Job Supplier Quotes"),
            ]
            vals = {"pages": pages}
            return request.render("supplier_portal.portal_home", vals)
        else:
            vals = {"supplier": supplier}
            return request.render("supplier_portal.portal_request_access", vals)

    @http.route(
        ["/vendor_request_access/<string:supplier_ref>"],
        type="http",
        auth="public",
        website=True,
        methods=["GET"],
    )
    def portal_request_access_vendor_rfq(self, supplier_ref, **kw):
        supplier = (
            request.env["ship.supplier"].sudo().search([("ref", "=", supplier_ref)])
        )

        if supplier:
            supplier.send_email_response_portal_request_access()
            return request.render(
                "supplier_portal.portal_request_access_sent",
                {"supplier": supplier},
            )
        else:
            return request.not_found(
                "Supplier not found. Please contact us for support."
            )
