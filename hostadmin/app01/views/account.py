#! /usr/bin/env python
# -*- coding:utf-8 -*-
from django.shortcuts import redirect, render
from app01.models import UserInfo
from rbac.service.init_permission import init_permission


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')

    username = request.POST.get('username')
    password = request.POST.get('password')
    current_user = UserInfo.objects.filter(username=username, password=password).first()

    if not current_user:
        return render(request, 'login.html', {'error': '用户名或密码错误'})

    init_permission(current_user, request)

    return redirect('/index/')


def logout(request):
    request.session.delete()
    return redirect('/login/')


def index(request):
    return render(request, 'index.html')
