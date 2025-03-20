from django.db import models


class Todo(models.Model):
    user = models.ForeignKey(to='auth.user', on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=1024)
    goal_set_date = models.DateField()
    set_to_complete = models.DateField()
    is_complete = models.BooleanField()