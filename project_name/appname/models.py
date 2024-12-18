from django.db import models



class ModelName(models.Model): #id  (update, delete)
    field1 = models.CharField(max_length=100)
    field2 = models.CharField(max_length=50, blank=True, null=True, help_text="enter name of field")

    def __str__(self):
        return self.field1
    




