from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200, blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    hierarchy = models.IntegerField(unique=True)
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    link = models.URLField(max_length=200, blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Test(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    title = models.CharField(max_length=200, blank=True, null=True)
    kurator = models.TextField(blank=True, null=True)
    diser_name = models.TextField(blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    hierarchy = models.IntegerField(unique=True)

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

    title = models.CharField(max_length=200, blank=True, null=True)
    kurator = models.TextField(blank=True, null=True)
    diser_name = models.TextField(blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    hierarchy = models.IntegerField(unique=True)

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
    title = models.CharField(max_length=200, blank=True, null=True)
    kurator = models.TextField(blank=True, null=True)
    diser_name = models.TextField(blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    hierarchy = models.IntegerField(unique=True)
    tests = models.ManyToManyField(
        to=Test,
        related_name='aspirants', blank=True, null=True)
    intrestings = models.ManyToManyField(
        to=Intresting,
        related_name='aspirants', blank=True, null=True)
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title



