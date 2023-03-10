# Generated by Django 4.1.6 on 2023-02-05 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="MyDetail",
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
                ("name", models.CharField(max_length=255)),
                ("education_details", models.TextField(blank=True, null=True)),
                ("technical_skill", models.CharField(max_length=255)),
                ("working_experience", models.IntegerField(default=1)),
            ],
        ),
    ]
