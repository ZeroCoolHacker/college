# Generated by Django 4.1.7 on 2023-02-17 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0004_alter_teacher_contact_number_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='id',
        ),
        migrations.AddField(
            model_name='teacher',
            name='teacher_id',
            field=models.BigAutoField(default=1, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='contact_number',
            field=models.PositiveBigIntegerField(),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='teacher_class',
            field=models.CharField(choices=[('ICS-P1', 'ICS-PART1'), ('M-P2', 'MEDICAL-PART2'), ('NM-P1', 'NON-MEDICAL-PART2'), ('M-P1', 'MEDICAL-PART1'), ('NM-P2', 'NON-MEDICAL-PART2'), ('ICS-P2', 'ICS-PART2')], max_length=10),
        ),
    ]
