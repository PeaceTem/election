# Generated by Django 4.2.1 on 2023-05-31 04:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("polling", "0019_polling_unit_date_entered"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="agentname", options={"verbose_name_plural": "agentnames"},
        ),
        migrations.AlterModelOptions(
            name="announced_lga_results",
            options={"verbose_name_plural": "announced_lga_results"},
        ),
        migrations.AlterModelOptions(
            name="announced_pu_results",
            options={"verbose_name_plural": "announced_pu_results"},
        ),
        migrations.AlterModelOptions(
            name="announced_state_results",
            options={"verbose_name_plural": "announced_state_results"},
        ),
        migrations.AlterModelOptions(
            name="announced_ward_results",
            options={"verbose_name_plural": "announced_ward_results"},
        ),
        migrations.AlterModelOptions(
            name="lga", options={"verbose_name_plural": "lgas"},
        ),
        migrations.AlterModelOptions(
            name="party", options={"verbose_name_plural": "parties"},
        ),
        migrations.AlterModelOptions(
            name="polling_unit", options={"verbose_name_plural": "polling_units"},
        ),
        migrations.AlterModelOptions(
            name="states", options={"verbose_name_plural": "states"},
        ),
        migrations.AlterModelOptions(
            name="ward", options={"verbose_name_plural": "wards"},
        ),
        migrations.AddField(
            model_name="lga",
            name="date_entered",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
    ]
