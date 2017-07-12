from django.conf.urls import  url
from web import views


urlpatterns = [
    url(r'^login/',views.login, name = 'login' ),
    url(r'^home/',views.home, name = 'home' ),
    url(r'^logout/',views.logout, name = 'logout' ),
    url(r'^createuser/',views.createuser, name = 'createuser' ),
    url(r'^edituser/',views.edituser, name = 'edituser' ),
    url(r'^createconection/',views.createconection, name = 'createconection' ),
    url(r'^connectionlist/',views.connectionlist, name = 'connectionlist' ),
    url(r'^gettables/',views.gettables, name = 'gettables' ),
    url(r'^getsentences/',views.getsentences, name = 'getsentences' ),
    # url(r'^order/',views.order, name = 'order' ),
    # url(r'^generatebill/',views.generatebill, name = 'generatebill' ),
    # url(r'^inventories/',views.inventories, name = 'inventories' ),
    # url(r'^accounting/',views.accounting, name = 'accounting' ),

]