# Generated by Django 5.0.1 on 2024-01-23 16:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_blogpost_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogpost',
            old_name='author',
            new_name='user',
        ),
    ]
