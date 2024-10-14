from django.db import models


class School(models.Model):

    school_name = models.CharField("School Name", max_length=256, blank=False)
    district = models.CharField("District", max_length=256, blank=False)

    school_address = models.CharField("Address", max_length=256, blank=False)

    advisor_name = models.CharField("Advisor Name", max_length=256, blank=False)
    advisor_email = models.CharField("Advisor Email", max_length=256, blank=False)
    advisor_phone_number = models.CharField("Advisor Phone Number", max_length=256, blank=False)
    advisor_emergency_contact = models.CharField("Emergency Contact", max_length=256, blank=False)
    advisor_emergency_contact_phone = models.CharField("Emergency Contact Phone Number", max_length=256,
            blank=False)

    def __str__(self):
        return f"{self.school_name}, {self.advisor_name}"
    

# Create your models here.
