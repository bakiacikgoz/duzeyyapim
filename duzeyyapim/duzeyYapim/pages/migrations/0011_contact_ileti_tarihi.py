# Generated by Django 4.1.3 on 2022-11-08 15:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0010_alter_contact_options_alter_contact_first_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='ileti_tarihi',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]