# Generated by Django 3.0.2 on 2020-02-12 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arguments', '0003_auto_20200212_0733'),
    ]

    operations = [
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('argument_id', models.CharField(max_length=120)),
                ('situation', models.CharField(max_length=120)),
                ('action', models.CharField(max_length=120)),
                ('goal', models.CharField(max_length=120)),
                ('value', models.CharField(max_length=120)),
                ('explanation', models.CharField(max_length=120)),
            ],
        ),
        migrations.DeleteModel(
            name='Yallah',
        ),
    ]
