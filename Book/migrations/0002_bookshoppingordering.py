# Generated by Django 2.0 on 2019-11-12 06:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Book', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookShoppingOrdering',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.CharField(max_length=64)),
                ('order_status', models.IntegerField(choices=[(0, '未支付'), (1, '已支付')], default=0)),
                ('goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Book.BookName')),
            ],
        ),
    ]
