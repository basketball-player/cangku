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


class CityInfos(models.Model):
    city = models.CharField(max_length=255, blank=True, null=True)
    mds = models.FloatField(db_column='MdS', blank=True, null=True)  # Field name made lowercase.
    td = models.DecimalField(db_column='TD', max_digits=32, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    nd = models.DecimalField(db_column='ND', max_digits=32, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    bd = models.DecimalField(db_column='BD', max_digits=32, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'city_infos'


class CityMds(models.Model):
    city = models.CharField(max_length=255, blank=True, null=True)
    mds = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'city_mds'


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
    jn = models.CharField(db_column='JN', max_length=255, blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(max_length=255, blank=True, null=True)
    wy = models.IntegerField(db_column='WY', blank=True, null=True)  # Field name made lowercase.
    ar = models.IntegerField(db_column='AR', blank=True, null=True)  # Field name made lowercase.
    number = models.IntegerField(blank=True, null=True)
    date = models.CharField(max_length=255, blank=True, null=True)
    msr = models.CharField(db_column='MSR', max_length=255, blank=True, null=True)  # Field name made lowercase.
    jc = models.CharField(db_column='JC', max_length=255, blank=True, null=True)  # Field name made lowercase.
    wf = models.CharField(db_column='WF', max_length=255, blank=True, null=True)  # Field name made lowercase.
    cl = models.CharField(db_column='CL', max_length=255, blank=True, null=True)  # Field name made lowercase.
    cm = models.CharField(db_column='CM', max_length=255, blank=True, null=True)  # Field name made lowercase.
    contact = models.CharField(db_column='Contact', max_length=255, blank=True, null=True)  # Field name made lowercase.
    jd = models.CharField(db_column='JD', max_length=16383, blank=True, null=True)  # Field name made lowercase.
    msl = models.FloatField(db_column='MSL', blank=True, null=True)  # Field name made lowercase.
    msh = models.FloatField(db_column='MSH', blank=True, null=True)  # Field name made lowercase.
    msm = models.FloatField(db_column='MSM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'fulltable'


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
