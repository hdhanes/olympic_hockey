# Generated by Django 4.1 on 2023-04-30 00:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('olympic', '0009_faceoffs_id_alter_faceoffs_faceoff_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shots',
            name='destination',
        ),
    ]
