from django.contrib import admin
from omaf_app.models import School, Team

# Register your models here.


class SchoolAdmin(admin.ModelAdmin):
    list_display = [
            "school_name",
            "advisor_name",
            "advisor_email",
            "advisor_phone_number",
            "advisor_emergency_contact",
            "advisor_emergency_contact_phone",

            ]


class TeamAdmin(admin.ModelAdmin):

    list_display = [
            "category",
            "school",
            "team_name",
            "students",
            "place",
            "flash_drive",
            "school__advisor_name",
            "onsite_competition",

    ]

    list_editable = ["place"]
    ordering = ["category", "school", "team_name"]




admin.site.register(School, SchoolAdmin)
admin.site.register(Team, TeamAdmin)


