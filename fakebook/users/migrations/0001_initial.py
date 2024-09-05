# Generated by Django 5.1.1 on 2024-09-04 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="UserProfile",
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
                ("username", models.CharField(max_length=32, unique=True)),
                ("password", models.CharField(max_length=256)),
                ("avatar", models.ImageField(null=True, upload_to="avatars")),
                ("bio", models.TextField(max_length=256, null=True)),
            ],
        ),
    ]