# Generated by Django 2.2.13 on 2020-09-16 14:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("licenses", "0004_auto_20200902_1302"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="translatedlicensename", unique_together=None,
        ),
        migrations.RemoveField(model_name="translatedlicensename", name="license",),
        migrations.DeleteModel(name="LicenseLogo",),
        migrations.DeleteModel(name="TranslatedLicenseName",),
    ]