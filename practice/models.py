from django.db import models

# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

class Customer(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    SHIRT_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large')
    )
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES)

class Group(models.Model):
    name = models.CharField(max_length=128)

class Blog(models.Model):
    name = models.CharField(max_length=100)


class Comment(models.Model):
    # Blog : Comment = 일대다
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    content = models.TextField()



