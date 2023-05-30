# Generated by Django 4.2.1 on 2023-05-30 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("polling", "0004_announced_pu_results"),
    ]

    operations = [
        migrations.CreateModel(
            name="announced_state_results",
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
                ("state_name", models.CharField(max_length=50)),
                ("party_abbreviation", models.CharField(max_length=4)),
                ("party_score", models.PositiveIntegerField()),
                ("entered_by_user", models.CharField(max_length=50)),
                ("date_entered", models.DateTimeField()),
                ("user_ip_address", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="announced_ward_results",
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
                ("ward_name", models.CharField(max_length=50)),
                ("party_abbreviation", models.CharField(max_length=4)),
                ("party_score", models.PositiveIntegerField()),
                ("entered_by_user", models.CharField(max_length=50)),
                ("date_entered", models.DateTimeField()),
                ("user_ip_address", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="lga",
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
                ("lga_id", models.PositiveIntegerField()),
                ("lga_name", models.CharField(max_length=50)),
                ("state_id", models.PositiveIntegerField()),
                ("lga_description", models.TextField(max_length=1000)),
                ("entered_by_user", models.CharField(max_length=50)),
                ("date_entered", models.DateTimeField()),
                ("user_ip_address", models.CharField(max_length=50)),
            ],
        ),
    ]
