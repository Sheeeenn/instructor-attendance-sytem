# Generated by Django 5.0.3 on 2024-04-12 15:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0020_attendancehistory_delete_deletedrecord'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AttendanceHistory',
        ),
    ]
