# Generated by Django 2.2 on 2019-09-14 17:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='pub_data',
            new_name='pub_date',
        ),
    ]