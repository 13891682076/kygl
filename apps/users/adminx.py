import xadmin
from xadmin.views import BaseAdminView, CommAdminView


@xadmin.sites.register(BaseAdminView)
class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


@xadmin.sites.register(CommAdminView)
class GlobalSettings(object):
    site_title = "城固客运后台管理系统"
    site_footer="www.keyun.com"
    menu_style = "accordion"
