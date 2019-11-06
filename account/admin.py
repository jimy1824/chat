import csv
from django.contrib import admin
from django.http import HttpResponse
from django.utils.html import format_html

from account.models import User


class Account(admin.ModelAdmin):
    list_display = (
        'id', 'created_at', 'is_active', 'first_name', 'last_name', 'gender', 'email', 'profile_image',)
    list_display_links = ('first_name', 'last_name', 'email',)
    list_filter = ['gender', 'is_active', ]
    search_fields = ('id', 'first_name', 'email')
    ordering = ['-id', ]
    date_hierarchy = 'created_at'
    fieldsets = (
        (None, {'fields': ('email', 'password', 'first_name', 'last_name', 'gender',
                           'profile_picture')}),
        ('Advanced options', {'classes': ('collapse',), 'fields': (
            'username', 'is_staff', 'is_active', 'is_superuser', 'user_permissions',
            'groups'), }),
    )
    actions = ["export_as_csv"]

    def export_as_csv(self, request, queryset):
        field_names = ['created_at', 'first_name', 'last_name', 'email', ]
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=usersreport.csv'.format(field_names)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            fields_list = []
            for field in field_names:
                fields_list.append(str(getattr(obj, field)))
            writer.writerow(fields_list)

        return response

    export_as_csv.short_description = "Export Selected"

    def profile_image(self, obj):
        return format_html(
            '<img style="width:50px; height:50px;border-radius:50%; " src="{}" >',
            obj.profile_picture.url if obj.profile_picture else None,
        )

    def save_model(self, request, obj, form, change):
        if obj.pk:
            orig_obj = User.objects.get(pk=obj.pk)
            if obj.password != orig_obj.password:
                obj.set_password(obj.password)
        else:
            obj.set_password(obj.password)
        obj.save()


admin.site.register(User, Account)
