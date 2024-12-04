from django.contrib import admin
from omaf_app.models import School, Team, Advisor, Student

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

class StudentInline(admin.TabularInline):
    model = Student


class TeamAdmin(admin.ModelAdmin):

    list_display = [
            "category",
            "school",
            "team_name",
            "students",
            "advisor",
            "onsite_competition",
            "place",
    ]

    list_display_links = [
            "school",
            "team_name",
            "advisor",
            "onsite_competition",

            ]

    inlines = [StudentInline]


    list_editable = ["place"]
    ordering = ["category", "advisor__school__school_name", "team_name"]

    def school(self, obj):
        return f"{obj.advisor.school}"

    def advisor(self, obj):
        return f"{obj.advisor.first_name} {obj.advisor.last_name}"

    def students(self, obj):
        students = obj.student_set.all()
        return ", ".join([x.student_name for x in students])





class StudentAdmin(admin.ModelAdmin):
    list_display = [
            "student_name",
            "shirt_size",
            "team",
            "advisor",
            "school",

            ]

    # @admin.display()

    def advisor(self, obj):
        return f"{obj.team.advisor}"

    def team(self, obj):
        return f"{obj.team.team_name}"

    def school(self, obj):
        return f"{obj.team.advisor.school.school_name}"


admin.site.register(School, SchoolAdmin)
admin.site.register(Advisor, AdvisorAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(Student, StudentAdmin)


