# Generated by Django 4.2.9 on 2024-01-06 17:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ExpenseGroups',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
                ('description', models.TextField(blank=True, null=True)),
                ('force_settled', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Expenses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
                ('description', models.TextField(blank=True, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('type', models.CharField(choices=[('EXPENSE', 'Expense'), ('SETTLEMENT', 'Settlement')], max_length=10)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='splitit_api.expensegroups')),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Spenders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=3, max_digits=10)),
                ('expense', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='splitit_api.expenses')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='splitit_api.users')),
            ],
        ),
        migrations.CreateModel(
            name='GroupMemberships',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='splitit_api.expensegroups')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='splitit_api.users')),
            ],
        ),
        migrations.AddField(
            model_name='expenses',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='splitit_api.users'),
        ),
        migrations.AddField(
            model_name='expensegroups',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='splitit_api.users'),
        ),
        migrations.CreateModel(
            name='Borrowers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=3, max_digits=10)),
                ('expense', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='splitit_api.expenses')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='splitit_api.users')),
            ],
        ),
    ]