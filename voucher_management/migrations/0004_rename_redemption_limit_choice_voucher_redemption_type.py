# Generated by Django 5.0.1 on 2024-01-19 10:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('voucher_management', '0003_remove_voucher_redemption_limit_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='voucher',
            old_name='redemption_limit_choice',
            new_name='redemption_type',
        ),
    ]
