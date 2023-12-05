# Generated by Django 4.2.4 on 2023-10-12 10:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="login",
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
                ("username", models.CharField(max_length=30)),
                ("email", models.CharField(max_length=30)),
                ("password", models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name="teacherregister",
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
                ("password", models.CharField(max_length=50)),
                ("email", models.EmailField(max_length=30, unique=True)),
                ("course", models.CharField(max_length=30)),
                ("department", models.CharField(max_length=30)),
                ("name", models.CharField(max_length=30)),
                ("subject", models.CharField(max_length=30)),
                ("role", models.CharField(max_length=10)),
                ("phone", models.CharField(max_length=10, unique=True)),
                (
                    "log_id",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE, to="Loginapp.login"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="studentregister",
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
                ("password", models.CharField(max_length=50)),
                ("email", models.EmailField(max_length=30, unique=True)),
                ("course", models.CharField(max_length=30)),
                ("department", models.CharField(max_length=30)),
                ("name", models.CharField(max_length=30)),
                ("subject", models.CharField(max_length=30)),
                ("role", models.CharField(max_length=10)),
                ("phone", models.CharField(max_length=10, unique=True)),
                (
                    "login_id",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE, to="Loginapp.login"
                    ),
                ),
            ],
        ),
    ]
