# Generated by Django 3.0.dev20190905135652 on 2019-09-18 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('financas', '0003_auto_20190917_2057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movimento',
            name='valor',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=12),
        ),
    ]
