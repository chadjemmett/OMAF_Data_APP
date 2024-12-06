from django.shortcuts import render
import csv
from django.http import HttpResponse
from . models import Student, School, Advisor, Team

# Create your views here.

CATEGORIES = {
            "bnp": "Broadcast News Package",
            "ba": "Broadcast Anchor",
            "pf": "Photography Fashion",
            "pcr": "Photograpy Creative",
            "pcm": "Photography Commercial",
            "pst": "Photography Street",
            "vre": "Video Convention Recap",
            "vpsa": "Video Public Service Announcment",
            "fftf": "Film Finish the Film",
            "f3m": "Film 3 Minutes",
            "f30": "Film 30 Seconds",
            "sm": "Social Media Instagram",
            "gd": "Graphic Design, Digital",
            "pj": "Print News Reporting",
            "pld": "Print Publication Layout & Design",
            }

def export(requests):
    response = HttpResponse(
            content_type ="text/csv",
            headers={"Content-Disposition": 'attachment; filename="team_List_download.csv"'}

            )

    team_list = Team.objects.all()
    writer = csv.writer(response)
    writer.writerow([
        "Category",
        "School",
        "Team Name",
        "Team Members",
        "Place",
        ])
    for t in team_list:
        students = Student.objects.filter(team_id=t.id)
        writer.writerow([
            CATEGORIES[t.category],  
            t.advisor.school,
            t.team_name,
            ", ".join([x.student_name for x in students])
        ])
    return response


def download(request):

    teams = Team.objects.exclude(place=None)
    context = {"teams_list": teams}
    return render (request, "omaf_app/downloads.html", context)


    # teams = Team.objects.where(place=True)
    


    
