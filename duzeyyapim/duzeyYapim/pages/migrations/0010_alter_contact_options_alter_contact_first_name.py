# Generated by Django 4.1.3 on 2022-11-08 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0009_alter_contact_dept_alter_contact_email_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contact',
            options={'verbose_name_plural': 'Gelen Formlar'},
        ),
        migrations.AlterField(
            model_name='contact',
            name='first_name',
            field=models.CharField(max_length=100, verbose_name='Adı ve Soyadı'),
        ),
    ]
