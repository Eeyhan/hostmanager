from django.shortcuts import render, redirect, HttpResponse
from app01.models import Host
from app01.forms import host
from rbac.service.urls import memory_reverse


def host_list(request):
    hosts = Host.objects.all()
    return render(request, 'host_list.html', {'hosts': hosts})


def host_add(request):
    if request.method == 'GET':
        form = host.HostModelForm()
        return render(request, 'rbac/change.html', {'form': form})
    form = host.HostModelForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect(memory_reverse(request, 'host_list'))
    return render(request, 'rbac/change.html', {'form': form})


def host_edit(request, id):
    obj = Host.objects.filter(id=id).first()
    if not obj:
        return HttpResponse('不存在该用户')

    if request.method == 'GET':
        form = host.HostModelForm(instance=obj)
        return render(request, 'rbac/change.html', {'form': form})
    form = host.HostModelForm(instance=obj, data=request.POST)
    if form.is_valid():
        form.save()
        return redirect(memory_reverse(request, 'host_list'))
    return render(request, 'rbac/change.html', {'form': form})


def host_del(request, id):
    cancel = memory_reverse(request, 'host_list')
    if request.method == 'GET':
        return render(request, 'rbac/delete.html', {'cancel': cancel})

    Host.objects.filter(id=id).delete()
    return redirect(cancel)
