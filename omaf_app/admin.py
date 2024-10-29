from django.contrib import admin
from omaf_app.models import School, Team, Advisor

# Register your models here.


class SchoolAdmin(admin.ModelAdmin):
    list_display = [
            "school_name",
            "district",
            "school_address",
            

            ]

class AdvisorAdmin(admin.ModelAdmin):
    list_display = [
            "advisor_name",
            "advisor_phone_number",
            "school__school_name",
            "school__principal"
            ]

class TeamAdmin(admin.ModelAdmin):

    list_display = [
            "category",
            "advisor__school__school_name",
            "team_name",
            "place",
            "advisor__advisor_name",
            "onsite_competition",

    ]

    list_editable = ["place"]
    ordering = ["category", "advisor__school__school_name", "team_name"]




admin.site.register(School, SchoolAdmin)
admin.site.register(Advisor, AdvisorAdmin)
admin.site.register(Team, TeamAdmin)


