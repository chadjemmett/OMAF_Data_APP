from django.db import models


class School(models.Model):

    school_name = models.CharField("School Name", max_length=256, blank=False, unique=True)
    district = models.CharField("District", max_length=256, blank=False)

    school_address = models.CharField("Address", max_length=256, blank=False)

    advisor_name = models.CharField("Advisor Name", max_length=256, blank=False)
    advisor_email = models.CharField("Advisor Email", max_length=256, blank=False)
    advisor_phone_number = models.CharField("Advisor Phone Number", max_length=256, blank=False)
    advisor_emergency_contact = models.CharField("Emergency Contact", max_length=256, blank=False)
    advisor_emergency_contact_phone = models.CharField("Emergency Contact Phone Number", max_length=256,
            blank=False)

    def __str__(self):
        return f"{self.school_name}"
   

class Team(models.Model):
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

    PLACE = {

            "1st": "First Place",
            "2nd": "Second Place",
            "3rd": "Third Place",
        }
    #belongs to
    school = models.ForeignKey(School, on_delete=models.CASCADE)

    team_name = models.CharField("Team Name", max_length=256, blank=False)
    onsite_competition = models.BooleanField(default=True)
    category = models.CharField(choices=CATEGORIES, blank=False, max_length=256)
    #will probably need a students model for tshirt size and conact information
    students = models.TextField(max_length=512, blank=False)
    place = models.CharField(choices=PLACE, blank=True, max_length=256)
    flash_drive = models.CharField("Flash Drive Size", max_length=256)

    def __str__(self):
        return self.team_name
    
    

class Student(models.Model):
    SHIRT_SIZE = {
            "XS": "Extra Small",
            "S": "Small",
            "M": "Medium",
            "L": "Large",
            "XL": "Extra Large",
            "XXL": "Extra X Large",
            "NA": "No T-shirt",
            }
    first_name = models.CharField("First Name", max_length=256, blank=False)
    last_name = models.CharField("Last Name", max_length=256, blank=False)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, blank=True)
    t_shirt = models.CharField("T-Shirt size", choices=SHIRT_SIZE, max_length=32, blank=True)




