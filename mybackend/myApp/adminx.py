import xadmin
from myApp.models import FisherMan

class FisherManAdmin(object):
    list_display = ['id', 'user', 'name', 'phone', 'email', 'create_time']
    search_fields = ['name', 'phone', 'email']
    list_filter = ['name', 'phone', 'email']
    list_per_page = 10
    show_detail_fields = ['name']
    model_icon = 'fa fa-user'

xadmin.site.register(FisherMan, FisherManAdmin)
