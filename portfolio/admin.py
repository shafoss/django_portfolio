from django.contrib import admin
from django.apps import apps
from django.conf import settings


def auto_register(model):
    # Get all fields from model, but exclude autocreated reverse relations
    field_list = [f.name for f in model._meta.get_fields() if f.auto_created is False and f.is_relation is False]
    # Dynamically create ModelAdmin class and register it.
    my_admin = type('MyAdmin', (admin.ModelAdmin,),
                    {'list_display': field_list}
                    )
    try:
        admin.site.register(model, my_admin)
    except admin.sites.AlreadyRegistered as e:
        # This model is already registered
        print(e)


if settings.DEBUG:
    for model in apps.get_models():
        auto_register(model)
