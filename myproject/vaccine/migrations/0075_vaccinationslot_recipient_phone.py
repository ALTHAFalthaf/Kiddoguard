# Generated by Django 4.2.5 on 2024-04-02 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vaccine', '0074_vaccinationslot'),
    ]

    operations = [
        migrations.AddField(
            model_name='vaccinationslot',
            name='recipient_phone',
            field=models.CharField(default='', max_length=20),
        ),
    ]
