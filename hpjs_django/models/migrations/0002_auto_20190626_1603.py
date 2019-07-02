# Generated by Django 2.2.1 on 2019-06-26 16:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='parameter',
            old_name='parameter_name',
            new_name='name',
        ),
        migrations.AlterField(
            model_name='parameter',
            name='hpjs_model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='parameters', to='models.HPJS_Model'),
        ),
        migrations.AlterField(
            model_name='parametervalue',
            name='parameter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='parameter_value', to='models.Parameter'),
        ),
        migrations.AlterField(
            model_name='parametervalue',
            name='trial',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='parameter_value', to='models.Trial'),
        ),
        migrations.AlterField(
            model_name='trial',
            name='hpjs_model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trials', to='models.HPJS_Model'),
        ),
    ]