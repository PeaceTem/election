# Generated by Django 4.2.1 on 2023-05-30 20:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("polling", "0011_alter_announced_lga_results_date_entered_and_more"),
    ]

    operations = [
        migrations.RemoveField(model_name="lga", name="date_entered",),
        migrations.RemoveField(model_name="polling_unit", name="date_entered",),
        migrations.RemoveField(model_name="ward", name="date_entered",),
    ]