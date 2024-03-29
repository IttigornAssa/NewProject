# Generated by Django 2.0.6 on 2018-06-26 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_person_document'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='department',
        ),
        migrations.RemoveField(
            model_name='person',
            name='image',
        ),
        migrations.RemoveField(
            model_name='person',
            name='phone_number',
        ),
        migrations.AddField(
            model_name='person',
            name='abstract',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='author',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
