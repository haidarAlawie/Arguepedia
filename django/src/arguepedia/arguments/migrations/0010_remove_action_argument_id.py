# Generated by Django 3.0.2 on 2020-03-03 19:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('arguments', '0009_action_parent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='action',
            name='argument_id',
        ),
    ]
