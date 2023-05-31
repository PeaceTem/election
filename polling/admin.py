from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(agentname)
admin.site.register(announced_lga_results)
admin.site.register(announced_pu_results)
admin.site.register(announced_state_results)
admin.site.register(announced_ward_results)
admin.site.register(lga)
admin.site.register(party)
admin.site.register(polling_unit)
admin.site.register(states)
admin.site.register(ward)

