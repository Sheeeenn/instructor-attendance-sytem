# Generated by Django 5.1 on 2024-11-07 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0040_orgchartlist_chairperson_dcs_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='PositionDCS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Chairperson_DCS', models.CharField(blank=True, max_length=200, null=True)),
                ('Program_Chair_CS', models.CharField(blank=True, max_length=200, null=True)),
                ('Program_Chair_IT', models.CharField(blank=True, max_length=200, null=True)),
                ('Instructors', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='orgchartlist',
            name='Chairperson_DCS',
        ),
        migrations.RemoveField(
            model_name='orgchartlist',
            name='Instructors',
        ),
        migrations.RemoveField(
            model_name='orgchartlist',
            name='Program_Chair_CS',
        ),
        migrations.RemoveField(
            model_name='orgchartlist',
            name='Program_Chair_IT',
        ),
        migrations.AddField(
            model_name='orgchartlist',
            name='position_dcs',
            field=models.ManyToManyField(blank=True, to='webapp.positiondcs'),
        ),
    ]
