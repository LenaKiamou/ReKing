# Generated by Django 4.0.3 on 2022-04-03 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Real_Estate', '0002_alter_house_more_features'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='district',
            field=models.CharField(default=0, max_length=24, verbose_name='Περιοχή'),
            preserve_default=False,
        ),
    ]
