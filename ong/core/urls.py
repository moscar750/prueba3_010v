from django.urls import path, include
from .views import inicio, contacto, enviado, exito, login, gatos, perros, prov, form_proveedor,envio_proveedor, edit, actualizar_proveedor, eliminar, ProveedorViewset
from .viewsLogin import login2
from rest_framework import routers

router = routers.DefaultRouter()
router.register('proveedor', ProveedorViewset)

urlpatterns = [
    path('', inicio, name="inicio"),
    path('contacto', contacto, name="contacto"),
    path('enviado', enviado, name="enviado"),
    path('exito', exito, name="exito"),
    path('login', login, name="login"),
    path('seccion-gatos', gatos, name="gatos"),
    path('seccion-perros', perros, name="perros"),
    path('proveedor', prov, name="proveedor"),
    path('form-proveedor', form_proveedor, name="form-proveedor"),
    path('guardar-proveedor', envio_proveedor, name="guardar-proveedor"),
    path('editar-proveedor/<str:idProveedor>', edit, name="editar-proveedor"),
    path('actualizar_proveedor/<str:idProveedor>', actualizar_proveedor, name="actualizar-proveedor"),
    path('eliminar/<str:idProveedor>', eliminar, name="eliminar-proveedor"),
    path('api/', include(router.urls)),
    path('login2', login2, name="login2"),
]
