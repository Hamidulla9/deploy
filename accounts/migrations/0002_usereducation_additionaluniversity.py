# Generated by Django 5.1.7 on 2025-03-24 11:49

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserEducation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('oqigan_joyi', models.CharField(max_length=255)),
                ('nomi', models.CharField(max_length=255)),
                ('yonalish', models.CharField(max_length=255)),
                ('diplom_raqami', models.CharField(max_length=50)),
                ('diplom_fayli', models.FileField(upload_to='diploms/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AdditionalUniversity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('oqigan_joyi', models.CharField(max_length=255)),
                ('nomi', models.CharField(max_length=255)),
                ('yonalish', models.CharField(max_length=255)),
                ('diplom_raqami', models.CharField(max_length=50)),
                ('diplom_fayli', models.FileField(upload_to='diploms/')),
                ('user_education', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='additional_universities', to='accounts.usereducation')),
            ],
        ),
    ]
