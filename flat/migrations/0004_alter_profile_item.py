# Generated by Django 5.0.1 on 2024-03-05 20:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("flat", "0003_remove_profile_name_alter_profile_phone"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="item",
            field=models.ForeignKey(
                null=True, on_delete=django.db.models.deletion.CASCADE, to="flat.item"
            ),
        ),
    ]
