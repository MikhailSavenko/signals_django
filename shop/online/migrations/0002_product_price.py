# Generated by Django 5.1.4 on 2024-12-24 12:54

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("online", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="price",
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
