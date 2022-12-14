# Generated by Django 3.2 on 2022-11-14 15:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('permissions', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='city',
            options={'verbose_name_plural': 'Cities'},
        ),
        migrations.RenameField(
            model_name='city',
            old_name='modified_at',
            new_name='updated_at',
        ),
        migrations.RenameField(
            model_name='permission',
            old_name='modified_at',
            new_name='updated_at',
        ),
        migrations.AddField(
            model_name='state',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='state',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='permission',
            name='expiration_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='permission',
            name='issued_date',
            field=models.DateField(),
        ),
    ]
