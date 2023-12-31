# Generated by Django 4.1.7 on 2023-04-17 14:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('employee', '0002_employeeeducation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employeeeducation',
            name='company1_desig',
        ),
        migrations.RemoveField(
            model_name='employeeeducation',
            name='company1_name',
        ),
        migrations.RemoveField(
            model_name='employeeeducation',
            name='company2_desig',
        ),
        migrations.RemoveField(
            model_name='employeeeducation',
            name='company2_name',
        ),
        migrations.RemoveField(
            model_name='employeeeducation',
            name='company3_desig',
        ),
        migrations.RemoveField(
            model_name='employeeeducation',
            name='company3_name',
        ),
        migrations.RemoveField(
            model_name='employeeeducation',
            name='uompany1_duration',
        ),
        migrations.RemoveField(
            model_name='employeeeducation',
            name='uompany2_duration',
        ),
        migrations.RemoveField(
            model_name='employeeeducation',
            name='uompany3_duration',
        ),
        migrations.AddField(
            model_name='employeeeducation',
            name='class_XI',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='employeeeducation',
            name='class_XII',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='employeeeducation',
            name='doj',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='employeeeducation',
            name='gender',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='employeeeducation',
            name='pg',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='employeeeducation',
            name='ug',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='employeeeducation',
            name='yop_class_XI',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='employeeeducation',
            name='yop_class_XII',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='employeeeducation',
            name='yop_pg',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='employeeeducation',
            name='yop_ug',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.CreateModel(
            name='EmployeeExperience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company1_name', models.CharField(max_length=50, null=True)),
                ('company1_desig', models.CharField(max_length=50, null=True)),
                ('uompany1_duration', models.CharField(max_length=50, null=True)),
                ('company2_name', models.CharField(max_length=50, null=True)),
                ('company2_desig', models.CharField(max_length=50, null=True)),
                ('uompany2_duration', models.CharField(max_length=50, null=True)),
                ('company3_name', models.CharField(max_length=50, null=True)),
                ('company3_desig', models.CharField(max_length=50, null=True)),
                ('uompany3_duration', models.CharField(max_length=50, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
