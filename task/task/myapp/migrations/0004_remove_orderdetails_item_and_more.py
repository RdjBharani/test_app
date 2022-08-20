# Generated by Django 4.1 on 2022-08-20 05:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myapp', '0003_orderdetails_created_by'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderdetails',
            name='item',
        ),
        migrations.RemoveField(
            model_name='orderdetails',
            name='store_details',
        ),
        migrations.AddField(
            model_name='orderdetails',
            name='quantity',
            field=models.CharField(blank=True, default='', max_length=64),
        ),
        migrations.AddField(
            model_name='orderdetails',
            name='total_amount',
            field=models.CharField(blank=True, default='', max_length=64),
        ),
        migrations.CreateModel(
            name='StoreItemDetailsMapping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_createdby', to=settings.AUTH_USER_MODEL)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.itemdetails')),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.storedetails')),
                ('updated_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_updatedby', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'store_item_mapping',
            },
        ),
        migrations.AddField(
            model_name='orderdetails',
            name='product',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='myapp.storeitemdetailsmapping'),
            preserve_default=False,
        ),
    ]