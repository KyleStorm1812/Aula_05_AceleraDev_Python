from django.db import models
from django.core import validators


# Create your models here.


class User(models.Model):
    name = models.CharField('Name', max_length=50)
    last_login = models.DateTimeField('Last Login', auto_now='True')
    email = models.EmailField(
        'E-mail',
        max_length=254,
        validators=[validators.validate_email]  # validators=[EmailValidator()]
    )
    password = models.CharField(
        'Password',
        max_length=50,
        validators=[validators.MinValueValidator(8)]
    )


class Agent(models.Model):
    name = models.CharField('Name', max_length=50)
    status = models.BooleanField()
    env = models.CharField('Env', max_length=20)
    version = models.CharField('Version', max_length=5)
    address = models.GenericIPAddressField(
        'IP Address',
        max_length=39,
        validators=[validators.validate_ipv4_address]
    )


class Event(models.Model):
    LEVELS_CHOICES = [
        ('CRITICAL', 'Critical'),
        ('DEBUG', 'Debug'),
        ('ERROR', 'Error'),
        ('WARNING','Warning'),
        ('INFO','Info')
    ]
    level = models.CharField('Level', max_length=20, choices=LEVELS_CHOICES)
    data = models.TextField()
    arquivado = models.BooleanField('Arquivado')
    date = models.DateField('Date', auto_now='True')
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Group(models.Model):
    name = models.CharField('Group', max_length=50)


class GroupUser(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

