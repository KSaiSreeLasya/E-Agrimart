# Generated by Django 3.1.3 on 2022-04-30 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_auto_20220426_1704'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='sales',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
