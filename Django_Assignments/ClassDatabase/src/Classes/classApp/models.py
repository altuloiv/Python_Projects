from django.db import models

###Creating my object django Classes
class djangoClasses(models.Model):
    Title = models.CharField(max_length=60, blank=False) ##title input for the class
    CourseNumber = models.IntegerField(default="", blank=False) ##CourseNumber for courses
    InstructorName = models.CharField(max_length=60, default="", blank=False) ##instructor for the course
    Duration = models.FloatField(blank=False) ##how long the course is

    ###Shows the name of the objects as the tittle of the class. s
    objects = models.Manager
    def __str__(self):
        return self.Title