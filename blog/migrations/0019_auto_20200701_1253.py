# Generated by Django 3.0.7 on 2020-07-01 12:53

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0018_auto_20200701_1244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='about',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]