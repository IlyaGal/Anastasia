from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200, required=False)
    text = models.TextField()
    hierarchy = models.IntegerField(default=1)
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Test(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    title = models.CharField(max_length=200)
    kurator = models.TextField(default=1)
    diser_name = models.TextField(default=1)
    text = models.TextField()
    hierarchy = models.IntegerField(default=1)

    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Intresting(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    title = models.CharField(max_length=200)
    kurator = models.TextField(default=1)
    diser_name = models.TextField(default=1)
    text = models.TextField()
    hierarchy = models.IntegerField(default=1)

    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Aspirant(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    kurator = models.TextField(default=1)
    diser_name = models.TextField(default=1)
    text = models.TextField()
    hierarchy = models.IntegerField(default=1)
    tests = models.ManyToManyField(
        to=Test,
        related_name='aspirants')
    intrestings = models.ManyToManyField(
        to=Intresting,
        related_name='aspirants')
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title



