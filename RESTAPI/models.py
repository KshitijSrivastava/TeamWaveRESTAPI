from django.db import models

# Create your models here.

class UserData(models.Model):
    display_name = models.CharField(max_length=50)
    #profile_image = models.ImageField()
    user_type = models.CharField(max_length=256, default = 'not_registered')
    reputation = models.IntegerField(default=0)

    def __str__(self):
        return self.display_name


class Question(models.Model):
    title = models.CharField(max_length = 256)
    question_text = models.TextField()
    creation_date = models.DateField(auto_now_add = True)
    is_answered = models.BooleanField(default = False)
    question_user = models.ForeignKey('UserData', on_delete=models.CASCADE)


    def __str__(self):
        return self.title


class Answer(models.Model):
    question = models.ForeignKey('Question', on_delete=models.CASCADE)
    answer_user = models.ForeignKey('UserData', on_delete=models.CASCADE)
    text = models.TextField(max_length=256)
    created_date = models.DateField(auto_now = True)
