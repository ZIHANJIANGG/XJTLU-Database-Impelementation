# Generated by Django 4.1.3 on 2022-12-02 07:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("CRUD", "0005_test"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Test",
        ),
        migrations.RemoveField(
            model_name="course",
            name="learners",
        ),
    ]
