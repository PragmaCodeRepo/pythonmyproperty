# Generated by Django 3.2.7 on 2021-12-06 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deals', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='renovation_required',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='Yes', max_length=5, verbose_name='Renovation Required'),
        ),
    ]