from django.contrib.auth.models import User, Group
from django.db import transaction
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from ControlDeAcceso.views.mid_auth import AuthAbsView
from Empresa.models.models import Empresa


class EmpresasView(AuthAbsView):
    def get(self, request):
        empresas = Empresa.objects.all()
        return render(request, 'Empresa/index.html', {'empresas': empresas})


class EmpresaCrearView(AuthAbsView):
    def get(self, request):
        return render(request, 'Empresa/modal_crear_editar.html', datos_render())

    @transaction.atomic
    def post(self, request):
        empresa = Empresa.data_form_empresa(request.POST)
        empresa.save()
        return redirect(reverse('empresa:index'))


class EmpresaEditarView(AuthAbsView):
    def get(self, request, id):
        return render(request, 'Empresa/modal_crear_editar.html', datos_render(id))

    @transaction.atomic
    def post(self, request, id):
        empresa = Empresa.data_form_empresa(request.POST)
        empresa.id = id
        empresa.save(update_fields=['nit', 'nombre_empresa', 'nombre_comercial', 'direccion', 'telefono',
                                    'correo_electronico', 'url_web', 'pais', 'departamento', 'ciudad'])
        return redirect(reverse('empresa:index'))


class EmpresaEliminarView(AuthAbsView):
    @transaction.atomic
    def post(self, request, id):
        try:
            Empresa.objects.get(id=id).delete()
            return JsonResponse({"estado": "OK"})
        except:
            return JsonResponse({"estado": "error",
                                 "mensaje": 'No es posible realizar esta accion'})


def datos_render(id_empresa=None):
    usuarios = User.objects\
        .exclude(is_superuser=True)\
        .exclude(groups__in=[Group.objects.get(name='Usuario de Empresa')])\
        .values('id', 'first_name', 'last_name')
    datos = {'usuarios': usuarios, 'origen': 'CREAR'}
    if id_empresa:
        datos['empresa'] = Empresa.objects.get(id=id_empresa)
        datos['origen'] = 'EDITAR'
    return datos
