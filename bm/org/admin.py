from django.contrib import admin
from .models import engineerregister
from.models import farmerregistration
from.models import cropregistration
from.models import farmerquiries
from.models import contact
from.models import typesofcrops

# Register your models here.
admin.site.register(engineerregister),
admin.site.register(farmerregistration),
admin.site.register(cropregistration),
admin.site.register(farmerquiries),
admin.site.register(contact),
admin.site.register(typesofcrops)
