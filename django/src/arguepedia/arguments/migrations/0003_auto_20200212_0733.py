# Generated by Django 3.0.2 on 2020-02-12 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arguments', '0002_auto_20200212_0724'),
    ]

    operations = [
        migrations.AlterField(
            model_name='yallah',
            name='main_arg',
            field=models.CharField(max_length=120),
        ),
    ]
