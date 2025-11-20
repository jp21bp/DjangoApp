from django.db import models

# Create your models here.
### Recall, "on_delete" has 3 options:
    # CASCADE = deletes the object(row) containing the Foreign key
    # PROTECT = prevents deletion of the reference object(row)
    # RESTRICT = prevents deletion of reference object by raising "RestrictedError"

#### One to One Relationship
    # Assume that one college can only have 1 princpal
class College(models.Model):
    CollegeID = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    website = models.URLField()

class Principal(models.Model):
    CollegeID = models.OneToOneField(
        College,
        on_delete=models.CASCADE
    )
        #Assuming 1-1
    email = models.EmailField(max_length=50)

#### One-to-many relationships
    # Assume 1 college can have many students and teachers
        #Use "ForeignKey"


class Student(models.Model):
    StudentID = models.IntegerField(primary_key=True)
    college_id = models.ForeignKey(
        College,
        on_delete=models.CASCADE
    )
    years_in = models.FloatField()
    dob = models.DateField()


#### Many-to-many relaionships
    # Assume students have multi teachers and teachers have multi studnts
        # Use "ManytoManyField"
class Teacher(models.Model):
    TeacherID = models.IntegerField(primary_key=True)
    college_id = models.ForeignKey(
        College,
        on_delete=models.CASCADE
    )
    student = models.ManyToManyField(Student)
    last_clocked_in = models.DateTimeField()


