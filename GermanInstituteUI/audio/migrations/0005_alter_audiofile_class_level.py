# Generated by Django 4.2.7 on 2024-03-23 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audio', '0004_rename_class_title_audiofile_class_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audiofile',
            name='class_level',
            field=models.CharField(blank=True, choices=[('A1', 'A1'), ('A2', 'A2'), ('B1', 'B1'), ('B2', 'B2')], default='Not-Set', max_length=50, null=True),
        ),
    ]
