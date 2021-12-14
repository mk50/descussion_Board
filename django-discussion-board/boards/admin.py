from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Board,Topic
# Register your models here.
admin.site.register(Board)
admin.site.register(Topic)
admin.site.unregister(Group)
admin.site.site_header="admin panel"
admin.site.site_title="admin panel"