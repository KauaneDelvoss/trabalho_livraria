# Generated by Django 4.1 on 2022-10-10 11:25

import uuid

from django.db import migrations, models

import media.models.document
import media.models.image


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attachment_key', models.UUIDField(default=uuid.uuid4, help_text='Used to attach the document to another object. Cannot be used to retrieve the document file.', unique=True)),
                ('public_id', models.UUIDField(default=uuid.uuid4, help_text='Used to retrieve the document file itself. Should not be readable until the document is attached to another object.', unique=True)),
                ('file', models.FileField(upload_to=media.models.document.document_file_path)),
                ('description', models.CharField(blank=True, max_length=255)),
                ('uploaded_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attachment_key', models.UUIDField(default=uuid.uuid4, help_text='Used to attach the image to another object. Cannot be used to retrieve the image file.', unique=True)),
                ('public_id', models.UUIDField(default=uuid.uuid4, help_text='Used to retrieve the image itself. Should not be readable until the image is attached to another object.', unique=True)),
                ('file', models.ImageField(upload_to=media.models.image.image_file_path)),
                ('description', models.CharField(blank=True, max_length=255)),
                ('uploaded_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
