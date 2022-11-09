# Generated by Django 4.1.3 on 2022-11-08 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0008_alter_contact_dept'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='dept',
            field=models.CharField(max_length=100, verbose_name='Departman'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(max_length=100, verbose_name='E-Mail'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='first_name',
            field=models.CharField(max_length=100, verbose_name='Adı'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='message',
            field=models.TextField(blank=True, verbose_name='Mesaj'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.CharField(max_length=100, verbose_name='Telefon Numarası'),
        ),
    ]