# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('street_1', models.CharField(max_length=50, verbose_name=b'Street 1')),
                ('street_2', models.CharField(max_length=50, verbose_name=b'Street 2')),
                ('city', models.CharField(max_length=50, verbose_name=b'City')),
                ('state', models.CharField(max_length=50, verbose_name=b'State')),
                ('country', models.CharField(max_length=50, verbose_name=b'Country', choices=[(b'india', b'India'), (b'uk', b'UK'), (b'usa', b'USA'), (b'china', b'China'), (b'nepal', b'Nepal')])),
                ('zipcode', models.IntegerField(max_length=6, null=True, verbose_name=b'Zipcode', blank=True)),
                ('mobile', models.IntegerField(max_length=13, unique=True, null=True, verbose_name=b'Mobile', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name=b'School Name')),
                ('logo', models.ImageField(upload_to=b'media/', max_length=255, verbose_name=b'Logo')),
                ('website', models.CharField(max_length=50, null=True, verbose_name=b'Website', blank=True)),
                ('is_active', models.BooleanField(default=True, verbose_name=b'Is active')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('creator', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('owner', models.ForeignKey(related_name=b'Owners', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('SMARTnumber', models.CharField(max_length=50, unique=True, null=True, verbose_name=b'Smart Num.', blank=True)),
                ('first_name', models.CharField(max_length=50, verbose_name=b'First Name')),
                ('last_name', models.CharField(max_length=50, verbose_name=b'Last Name')),
                ('email', models.EmailField(unique=True, max_length=75, verbose_name=b'EmailID')),
                ('roll_no', models.PositiveIntegerField(unique=True, verbose_name=b'Roll No.')),
                ('date_of_birth', models.DateField(verbose_name=b'Birthdate')),
                ('is_active', models.BooleanField(default=True, verbose_name=b'Is active')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('address', models.ManyToManyField(to='school_mgmt.Address', null=True, blank=True)),
                ('school', models.ForeignKey(to='school_mgmt.School')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name=b'University')),
                ('website', models.CharField(max_length=50, null=True, verbose_name=b'Website', blank=True)),
                ('is_active', models.BooleanField(default=True, verbose_name=b'Is active')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='school',
            name='university',
            field=models.ForeignKey(to='school_mgmt.University'),
            preserve_default=True,
        ),
    ]
