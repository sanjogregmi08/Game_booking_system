# Generated by Django 4.0 on 2022-01-30 04:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('games', '0002_alter_games_image'),
        ('customer', '0002_rename_password_customer_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('booking_id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('date', models.CharField(max_length=50)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.customer')),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='games.games')),
            ],
        ),
    ]
