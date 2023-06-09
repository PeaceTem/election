# Generated by Django 4.2.1 on 2023-05-30 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("polling", "0003_alter_agentname_pollingunit_uniqueid_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="announced_pu_results",
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
                ("polling_unit_uniqueid", models.CharField(max_length=50)),
                ("party_abbreviation", models.CharField(max_length=4)),
                ("party_score", models.PositiveIntegerField()),
                ("entered_by_user", models.CharField(max_length=50)),
                ("date_entered", models.DateTimeField()),
                ("user_ip_address", models.CharField(max_length=50)),
            ],
        ),
    ]
