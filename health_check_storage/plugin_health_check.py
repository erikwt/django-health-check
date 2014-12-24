#-*- coding: utf-8 -*-
from django_health_check.health_check.plugins import plugin_dir
from django_health_check.health_check_storage.base import StorageHealthCheck
from django.conf import settings


class DefaultFileStorageHealthCheck(StorageHealthCheck):
    storage = settings.DEFAULT_FILE_STORAGE

plugin_dir.register(DefaultFileStorageHealthCheck)
