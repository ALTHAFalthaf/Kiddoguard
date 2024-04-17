# Generated by Django 4.2.5 on 2024-04-04 09:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vaccine', '0076_appointment_child'),
    ]

    operations = [
        migrations.CreateModel(
            name='VaccinePrescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vaccine_name', models.CharField(max_length=200)),
                ('doses', models.PositiveIntegerField()),
                ('comments', models.TextField(blank=True)),
                ('appointment', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='vaccine_prescription', to='vaccine.appointment')),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vaccine_prescriptions', to='vaccine.doctor')),
            ],
        ),
    ]