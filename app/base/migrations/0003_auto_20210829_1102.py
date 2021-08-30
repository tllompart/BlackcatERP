# Generated by Django 2.2.6 on 2021-08-29 11:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_erpuser_username'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PyChannel',
            new_name='Channel',
        ),
        migrations.RenameModel(
            old_name='PyComment',
            new_name='Comment',
        ),
        migrations.RenameModel(
            old_name='PyCron',
            new_name='Cron',
        ),
        migrations.RenameModel(
            old_name='PyImage',
            new_name='Faq',
        ),
        migrations.RenameModel(
            old_name='PyFaq',
            new_name='Image',
        ),
        migrations.AlterModelOptions(
            name='faq',
            options={'verbose_name': 'Faq', 'verbose_name_plural': 'Faqs'},
        ),
        migrations.AlterModelOptions(
            name='image',
            options={'verbose_name': 'Image', 'verbose_name_plural': 'PyImage'},
        ),
        migrations.RemoveField(
            model_name='pypost',
            name='img',
        ),
        migrations.AlterField(
            model_name='email',
            name='partner_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='base.Partner'),
        ),
    ]
