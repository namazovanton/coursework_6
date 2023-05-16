# Generated by Django 3.2.6 on 2023-05-15 21:00

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=12, region=None)),
                ('email', models.EmailField(max_length=40, null=True, unique=True)),
                ('role', models.CharField(choices=[('user', 'User'), ('admin', 'Admin')], default='user', max_length=5)),
                ('is_active', models.BooleanField(default=False)),
                ('image', models.ImageField(blank=True, null=True, upload_to='user_pics')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
