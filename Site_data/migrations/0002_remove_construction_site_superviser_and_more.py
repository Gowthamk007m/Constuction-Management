# Generated by Django 4.1.7 on 2023-03-30 06:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Site_data', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='construction_site',
            name='superviser',
        ),
        migrations.RemoveField(
            model_name='site_user',
            name='fullname',
        ),
        migrations.RemoveField(
            model_name='site_user',
            name='image',
        ),
        migrations.AddField(
            model_name='site_user',
            name='site_data',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Site_data.construction_site'),
            preserve_default=False,
        ),
    ]
