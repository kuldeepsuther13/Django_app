# Generated by Django 4.2.7 on 2023-11-24 10:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='patient',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app_users.patient'),
        ),
        migrations.AddField(
            model_name='result',
            name='patient',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app_users.patient'),
        ),
        migrations.AddField(
            model_name='result',
            name='test',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app_users.tests'),
        ),
        migrations.AddField(
            model_name='sample',
            name='patient',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app_users.patient'),
        ),
        migrations.AddField(
            model_name='sample',
            name='test',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app_users.tests'),
        ),
    ]
