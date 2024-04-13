{
    "name": "Facebook ecommerce",
    "author": "Hieu",
    "website": "www.hieu-ecommerce.tech",
    "summary": "Facebook ecommerce",
    "depends": ["mail", "website", "web_window_title"],
    "data": [
        "security/role.xml",
        "security/rule.xml",
        "security/ir.model.access.csv",
        "data/sequence.xml",
        "views/menu.xml",
        "views/task.xml",
        "views/inherit_view.xml",
        "reports/report.xml",
    ],
    "application": True,
    "assets": {
        "web.assets_backend": [
            "fb/static/css/my_css.css",
        ],
    },
}
