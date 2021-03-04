# Generated by Django 3.1.7 on 2021-03-04 09:34

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cafe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50, verbose_name='카페 이름')),
                ('address', models.CharField(default='', max_length=100, verbose_name='카페 주소')),
                ('is_registered', models.BooleanField(default=False, verbose_name='Cafe status')),
            ],
            options={
                'verbose_name': '카페',
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('update_date', models.DateTimeField(auto_now_add=True, verbose_name='리뷰 작성일')),
                ('score', models.IntegerField(default=3, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)], verbose_name='카페 별점')),
                ('password', models.CharField(default='', max_length=10, verbose_name='카페 비밀번호')),
                ('related_cafe', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cafe.cafe', verbose_name='대상 카페')),
            ],
            options={
                'verbose_name': '리뷰',
            },
        ),
    ]