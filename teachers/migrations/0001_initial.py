# Generated by Django 4.1.7 on 2023-02-17 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('date_of_birth', models.DateTimeField(blank=True, null=True)),
                ('teacher_class', models.CharField(choices=[('ICS-P2', 'ICS-PART2'), ('NM-P2', 'NON-MEDICAL-PART2'), ('M-P2', 'MEDICAL-PART2'), ('M-P1', 'MEDICAL-PART1'), ('ICS-P1', 'ICS-PART1'), ('NM-P1', 'NON-MEDICAL-PART2')], max_length=10)),
                ('joining_date', models.DateField(auto_now_add=True)),
                ('contact_number', models.SmallIntegerField(max_length=15)),
                ('still_joined', models.BooleanField(default=True)),
            ],
        ),
    ]
