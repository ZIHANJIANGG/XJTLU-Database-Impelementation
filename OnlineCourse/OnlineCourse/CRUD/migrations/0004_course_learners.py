# Generated by Django 4.1.3 on 2022-11-30 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("CRUD", "0003_alter_enrollment_date_enrolled"),
    ]

    operations = [
        migrations.AddField(
            model_name="course",
            name="learners",
            field=models.ManyToManyField(through="CRUD.Enrollment", to="CRUD.learner"),
        ),
    ]
