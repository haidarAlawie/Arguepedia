# Generated by Django 3.0.2 on 2020-03-03 20:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('arguments', '0013_auto_20200303_2022'),
    ]

    operations = [
        migrations.AddField(
            model_name='argumentpost',
            name='action',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='arguments.Action'),
        ),
    ]
