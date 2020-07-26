from django.contrib import admin
from .models import Team,Team_Members, Team_Sponsors, Images

admin.site.register(Team)
admin.site.register(Team_Members)
admin.site.register(Team_Sponsors)
admin.site.register(Images)
