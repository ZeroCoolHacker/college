from django.db import models
# Create your models here.
CLASS = {
    ("ICS-P1", "ICS-PART1"),
    ("ICS-P2", "ICS-PART2"),
    ("M-P1", "MEDICAL-PART1"),
    ("M-P2", "MEDICAL-PART2"),
    ("NM-P1", "NON-MEDICAL-PART2"),
    ("NM-P2", "NON-MEDICAL-PART2"),
}
class Teacher(models.Model):
    first_name = models.CharField(max_length= 30, null=False, blank=False)
    last_name = models.CharField(max_length= 30, null=False, blank=False)
    date_of_birth = models.DateTimeField(auto_now_add=False, auto_now=False, null=True, blank=True)
    teacher_class = models.CharField(max_length=10, choices=CLASS)
    joining_date = models.DateField(auto_now_add=True)
    contact_number = models.PositiveBigIntegerField(blank=False, null=False)
    still_joined = models.BooleanField(default=True)
    teacher_id = models.BigAutoField(primary_key=True)
    def __str__(self):
        return f"{self.first_name} -- {self.last_name} -- {self.joining_date}"
    
    
    

class Salary:
    pass


class Billing_history:
    pass
