# Generated by Django 3.0.7 on 2020-07-01 14:22

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0019_auto_20200701_1253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='about',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
    ]
