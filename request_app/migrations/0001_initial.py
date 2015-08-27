# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('client_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='FeatureRequest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200, verbose_name=b'Title')),
                ('description', models.TextField(verbose_name=b'Description')),
                ('priority', models.IntegerField(default=0, verbose_name=b'Priority')),
                ('target_date', models.DateField(max_length=10, verbose_name=b'Target Date')),
                ('tix_url', models.CharField(max_length=200, verbose_name=b'Ticket URL')),
                ('product_area', models.CharField(default=b'policies', max_length=10, verbose_name=b'Product Area', choices=[(b'policies', b'Policies'), (b'billing', b'Billing'), (b'claims', b'Claims'), (b'reports', b'Reports')])),
                ('body_html', models.TextField(blank=True)),
                ('client', models.ForeignKey(default=None, blank=True, to='request_app.Client', null=True, verbose_name=b'Client')),
            ],
            options={
                'ordering': ('-target_date', '-priority'),
            },
        ),
    ]
