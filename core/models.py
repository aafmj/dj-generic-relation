from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericRelation
from django.db.models import F


class Activity(models.Model):
    FAVORITE = 'F'
    LIKE = 'L'
    UP_VOTE = 'U'
    DOWN_VOTE = 'D'
    ACTIVITY_TYPES = (
        (FAVORITE, 'Favorite'),
        (LIKE, 'Like'),
        (UP_VOTE, 'Up Vote'),
        (DOWN_VOTE, 'Down Vote'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity_type = models.CharField(max_length=1, choices=ACTIVITY_TYPES)
    date = models.DateTimeField(auto_now_add=True)

    # Below the mandatory fields for generic relation
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()


class Post(models.Model):
    likes = GenericRelation(Activity)
    title = models.CharField(max_length=50, default=f"title {F('id')} of {F('__name__')}")

    def __str__(self):
        return self.title


class Question(models.Model):
    activities = GenericRelation(Activity)
    title = models.CharField(max_length=50, default=f"title {F('id')} of {F('__name__')}")

    def __str__(self):
        return self.title


class Answer(models.Model):
    title = models.CharField(max_length=50, default=f"title {F('id')} of {F('__name__')}")
    activities = GenericRelation(Activity)

    def __str__(self):
        return self.title


class Comment(models.Model):
    title = models.CharField(max_length=50, default=f"title {F('id')} of {F('__name__')}")

    def __str__(self):
        return self.title


class Person(models.Model):
    title = models.CharField(max_length=50, default=f"title" + str({F('id')}))
    job_positions = models.ManyToManyField("JobPosition", through="Job")


class Company(models.Model):
    title = models.CharField(max_length=50, default=f"title" + str({F('id')}))
    persons = models.ManyToManyField(Person, through="Job")


class JobPosition(models.Model):
    title = models.CharField(max_length=50, default=f"title" + str({F('id')}))


class Job(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    job_position = models.ForeignKey(JobPosition, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, default=f"title" + str({F('id')}))
