from django.urls import path

from Empresa.views import views, horario_acceso, punto_acceso

app_name = 'Empresa'


urlpatterns = [
    path('index', views.EmpresasView.as_view(), name='index'),
    path('crear', views.EmpresaCrearView.as_view(), name='crear'),
    path('editar/<int:id>', views.EmpresaEditarView.as_view(), name='editar'),
    path('eliminar/<int:id>', views.EmpresaEliminarView.as_view(), name='eliminar'),
    path('horario-acceso', horario_acceso.HorariosAccesosView.as_view(), name='horario-acceso'),
    path('horario-acceso/crear', horario_acceso.HorarioAccesoCrearView.as_view(), name='horario-acceso-crear'),
    path('horario-acceso/<int:id>/editar', horario_acceso.HorarioAccesoEditarView.as_view(),
         name='horario-acceso-editar'),
    path('horario-acceso/<int:id>/eliminar', horario_acceso.HorarioAccesoEliminarView.as_view(),
         name='horario-acceso-eliminar'),
    path('punto-acceso', punto_acceso.PuntosAccesosView.as_view(), name='punto-acceso'),
    path('punto-acceso/crear', punto_acceso.PuntoAccesoCrearView.as_view(), name='punto-acceso-crear'),
    path('punto-acceso/<int:id>/editar', punto_acceso.PuntoAccesoEditarView.as_view(), name='punto-acceso-editar'),
    path('punto-acceso/<int:id>/eliminar', punto_acceso.PuntoAccesoEliminarView.as_view(),
         name='punto-acceso-eliminar'),
]
