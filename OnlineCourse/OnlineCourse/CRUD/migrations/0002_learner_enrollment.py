# Generated by Django 4.1.3 on 2022-11-30 13:59

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("CRUD", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Learner",
            fields=[
                (
                    "user_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="CRUD.user",
                    ),
                ),
                (
                    "occupation",
                    models.CharField(
                        choices=[
                            ("student", "Student"),
                            ("developer", "Developer"),
                            ("data_scientist", "Data Scientist"),
                            ("dba", "Database Admin"),
                        ],
                        default="student",
                        max_length=20,
                    ),
                ),
                ("social_link", models.URLField()),
            ],
            bases=("CRUD.user",),
        ),
        migrations.CreateModel(
            name="Enrollment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "date_enrolled",
                    models.DateField(
                        default=datetime.datetime(2022, 11, 30, 13, 59, 5, 164639)
                    ),
                ),
                (
                    "mode",
                    models.CharField(
                        choices=[("audit", "Audit"), ("honor", "Honor")],
                        default="audit",
                        max_length=5,
                    ),
                ),
                (
                    "course",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="CRUD.course"
                    ),
                ),
                (
                    "learner",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="CRUD.learner"
                    ),
                ),
            ],
        ),
    ]
