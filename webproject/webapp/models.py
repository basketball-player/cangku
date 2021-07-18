# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Bdrnk(models.Model):
    city = models.CharField(max_length=255, blank=True, null=True)
    bdrnk = models.FloatField(db_column='BDrnk', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'bdrnk'


class CityInfo(models.Model):
    city = models.CharField(max_length=255, blank=True, null=True)
    ms = models.DecimalField(db_column='MS', max_digits=14, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    td = models.DecimalField(db_column='TD', max_digits=32, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    nd = models.DecimalField(db_column='ND', max_digits=32, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    bd = models.DecimalField(db_column='BD', max_digits=32, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'city_info'


class CityRnk(models.Model):
    city = models.CharField(max_length=255, blank=True, null=True)
    msrnk = models.FloatField(db_column='MSrnk', blank=True, null=True)  # Field name made lowercase.
    tdrnk = models.FloatField(db_column='TDrnk', blank=True, null=True)  # Field name made lowercase.
    ndrnk = models.FloatField(db_column='NDrnk', blank=True, null=True)  # Field name made lowercase.
    bdrnk = models.FloatField(db_column='BDrnk', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'city_rnk'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Fulltable(models.Model):
    jobtitle = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    workingyears = models.CharField(max_length=255, blank=True, null=True)
    academicrequirements = models.CharField(max_length=255, blank=True, null=True)
    number = models.IntegerField(blank=True, null=True)
    date = models.CharField(max_length=255, blank=True, null=True)
    monthlysalaryrange = models.CharField(max_length=255, blank=True, null=True)
    job = models.CharField(max_length=255, blank=True, null=True)
    welfare = models.CharField(max_length=255, blank=True, null=True)
    link = models.CharField(max_length=255, blank=True, null=True)
    companyname = models.CharField(max_length=255, blank=True, null=True)
    contact = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=12287, blank=True, null=True)
    minimum_monthlysalary = models.IntegerField(blank=True, null=True)
    maximum_monthlysalary = models.IntegerField(blank=True, null=True)
    mean_monthlysalary = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fulltable'


class FulltableCopy(models.Model):
    jobtitle = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    workingyears = models.CharField(max_length=255, blank=True, null=True)
    academicrequirements = models.CharField(max_length=255, blank=True, null=True)
    number = models.IntegerField(blank=True, null=True)
    date = models.CharField(max_length=255, blank=True, null=True)
    monthlysalaryrange = models.CharField(max_length=255, blank=True, null=True)
    job = models.CharField(max_length=255, blank=True, null=True)
    welfare = models.CharField(max_length=255, blank=True, null=True)
    link = models.CharField(max_length=255, blank=True, null=True)
    companyname = models.CharField(max_length=255, blank=True, null=True)
    contact = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=12287, blank=True, null=True)
    minimum_monthlysalary = models.IntegerField(blank=True, null=True)
    maximum_monthlysalary = models.IntegerField(blank=True, null=True)
    mean_monthlysalary = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fulltable_copy'


class MedianSalary(models.Model):
    city = models.CharField(max_length=255, blank=True, null=True)
    median_salary = models.DecimalField(max_digits=14, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'median_salary'


class Msrnk(models.Model):
    city = models.CharField(max_length=255, blank=True, null=True)
    msrnk = models.FloatField(db_column='MSrnk', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'msrnk'


class Ndrnk(models.Model):
    city = models.CharField(max_length=255, blank=True, null=True)
    ndrnk = models.FloatField(db_column='NDrnk', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ndrnk'


class Tdrnk(models.Model):
    city = models.CharField(max_length=255, blank=True, null=True)
    tdrnk = models.FloatField(db_column='TDrnk', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tdrnk'
