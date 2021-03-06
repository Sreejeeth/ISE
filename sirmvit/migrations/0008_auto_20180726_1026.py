# Generated by Django 2.0.7 on 2018-07-26 04:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sirmvit', '0007_studentdbs_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='studentdbs',
            options={'ordering': ('name',)},
        ),
        migrations.RenameField(
            model_name='studentdbs',
            old_name='USN',
            new_name='contact_no',
        ),
        migrations.RenameField(
            model_name='studentdbs',
            old_name='fifth',
            new_name='critical_research',
        ),
        migrations.RenameField(
            model_name='studentdbs',
            old_name='first',
            new_name='data_analysis',
        ),
        migrations.RenameField(
            model_name='studentdbs',
            old_name='fourth',
            new_name='domain',
        ),
        migrations.RenameField(
            model_name='studentdbs',
            old_name='address',
            new_name='email_address',
        ),
        migrations.RenameField(
            model_name='studentdbs',
            old_name='second',
            new_name='general_biology',
        ),
        migrations.RenameField(
            model_name='studentdbs',
            old_name='third',
            new_name='quality_control',
        ),
    ]
