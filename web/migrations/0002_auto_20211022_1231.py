# Generated by Django 3.2.8 on 2021-10-22 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='todolistitem',
            options={'ordering': ('content',)},
        ),
        migrations.AlterField(
            model_name='todolistitem',
            name='id',
            field=models.CharField(max_length=4, primary_key=True, serialize=False),
        ),
    ]
