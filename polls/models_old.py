# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

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
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
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


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
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


class PollsChoice(models.Model):
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField()
    question = models.ForeignKey('PollsQuestion', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'polls_choice'


class PollsQuestion(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'polls_question'


class PollsTApkSystemConfig(models.Model):
    project = models.CharField(max_length=30)
    version = models.CharField(max_length=20)
    systemsize = models.CharField(db_column='systemSize', max_length=11)  # Field name made lowercase.
    fixedsize = models.CharField(db_column='fixedSize', max_length=11)  # Field name made lowercase.
    surplussize = models.CharField(db_column='surplusSize', max_length=11)  # Field name made lowercase.
    hdversion = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'polls_t_apk_system_config'


class Roles(models.Model):
    username = models.CharField(max_length=15)
    rolename = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'roles'


class TApkInfo(models.Model):
    apk_id = models.AutoField(db_column='APK_ID', primary_key=True)  # Field name made lowercase.
    apkversion = models.CharField(db_column='APKVERSION', max_length=100, blank=True, null=True)  # Field name made lowercase.
    apkpath = models.CharField(db_column='APKPATH', max_length=400, blank=True, null=True)  # Field name made lowercase.
    platform = models.CharField(db_column='PLATFORM', max_length=400, blank=True, null=True)  # Field name made lowercase.
    heirname = models.CharField(db_column='HEIRNAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    apkname = models.CharField(db_column='APKNAME', max_length=300, blank=True, null=True)  # Field name made lowercase.
    filepath = models.CharField(db_column='FILEPATH', max_length=400, blank=True, null=True)  # Field name made lowercase.
    newdate = models.CharField(db_column='NEWDATE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    encrypt = models.CharField(db_column='ENCRYPT', max_length=100, blank=True, null=True)  # Field name made lowercase.
    userid = models.IntegerField(db_column='USERID', blank=True, null=True)  # Field name made lowercase.
    apktype = models.CharField(db_column='APKTYPE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    functionid = models.CharField(db_column='FUNCTIONID', max_length=400, blank=True, null=True)  # Field name made lowercase.
    project_name = models.CharField(db_column='PROJECT_NAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    project_id = models.CharField(db_column='PROJECT_ID', max_length=40, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_apk_info'


class TApkSystemConfig(models.Model):
    project = models.CharField(max_length=30, blank=True, null=True)
    version = models.CharField(max_length=20, blank=True, null=True)
    systemsize = models.IntegerField(db_column='systemSize', blank=True, null=True)  # Field name made lowercase.
    fixedsize = models.IntegerField(db_column='fixedSize', blank=True, null=True)  # Field name made lowercase.
    surplussize = models.IntegerField(db_column='surplusSize', blank=True, null=True)  # Field name made lowercase.
    hdversion = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_apk_system_config'


class TApktemplateInfo(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    apk_id = models.IntegerField(db_column='APK_ID', blank=True, null=True)  # Field name made lowercase.
    apkversion = models.CharField(db_column='APKVERSION', max_length=100, blank=True, null=True)  # Field name made lowercase.
    apkpath = models.CharField(db_column='APKPATH', max_length=400, blank=True, null=True)  # Field name made lowercase.
    platform = models.CharField(db_column='PLATFORM', max_length=400, blank=True, null=True)  # Field name made lowercase.
    heirname = models.CharField(db_column='HEIRNAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    apkname = models.CharField(db_column='APKNAME', max_length=300, blank=True, null=True)  # Field name made lowercase.
    filepath = models.CharField(db_column='FILEPATH', max_length=400, blank=True, null=True)  # Field name made lowercase.
    newdate = models.CharField(db_column='NEWDATE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    encrypt = models.CharField(db_column='ENCRYPT', max_length=100, blank=True, null=True)  # Field name made lowercase.
    userid = models.IntegerField(db_column='USERID', blank=True, null=True)  # Field name made lowercase.
    apktype = models.CharField(db_column='APKTYPE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    functionid = models.CharField(db_column='FUNCTIONID', max_length=400, blank=True, null=True)  # Field name made lowercase.
    project_name = models.CharField(db_column='PROJECT_NAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    project_id = models.CharField(db_column='PROJECT_ID', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tem_id = models.CharField(db_column='TEM_ID', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_apktemplate_info'


class TBChip(models.Model):
    chip_id = models.AutoField(db_column='CHIP_ID', primary_key=True)  # Field name made lowercase.
    chip_name = models.CharField(db_column='CHIP_NAME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    plat_id = models.CharField(db_column='PLAT_ID', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_b_chip'


class TBPlatform(models.Model):
    plat_id = models.AutoField(db_column='PLAT_ID', primary_key=True)  # Field name made lowercase.
    platform_name = models.CharField(db_column='PLATFORM_NAME', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_b_platform'


class TBProject(models.Model):
    pro_id = models.AutoField(db_column='PRO_ID', primary_key=True)  # Field name made lowercase.
    project_name = models.CharField(db_column='PROJECT_NAME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    plat_id = models.CharField(db_column='PLAT_ID', max_length=10, blank=True, null=True)  # Field name made lowercase.
    chip_id = models.CharField(db_column='CHIP_ID', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_b_project'


class TBaseInfo(models.Model):
    tid = models.IntegerField(db_column='TID')  # Field name made lowercase.
    updatever = models.CharField(db_column='UPDATEVER', max_length=150, blank=True, null=True)  # Field name made lowercase.
    softname = models.CharField(db_column='SOFTNAME', max_length=150, blank=True, null=True)  # Field name made lowercase.
    linename = models.CharField(db_column='LINENAME', max_length=120, blank=True, null=True)  # Field name made lowercase.
    tfver = models.CharField(db_column='TFVER', max_length=150, blank=True, null=True)  # Field name made lowercase.
    tfbyte = models.CharField(db_column='TFBYTE', max_length=33, blank=True, null=True)  # Field name made lowercase.
    folderqty = models.CharField(db_column='FOLDERQTY', max_length=33, blank=True, null=True)  # Field name made lowercase.
    fileqty = models.CharField(db_column='FILEQTY', max_length=33, blank=True, null=True)  # Field name made lowercase.
    valid = models.CharField(db_column='VALID', max_length=33, blank=True, null=True)  # Field name made lowercase.
    uploadstatus = models.CharField(db_column='UPLOADSTATUS', max_length=12, blank=True, null=True)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CREATEDDATE', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CREATEDBY', max_length=60, blank=True, null=True)  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='MODIFIEDDATE', blank=True, null=True)  # Field name made lowercase.
    modifiedby = models.CharField(db_column='MODIFIEDBY', max_length=33, blank=True, null=True)  # Field name made lowercase.
    updatestate = models.CharField(db_column='UPDATESTATE', max_length=12, blank=True, null=True)  # Field name made lowercase.
    linetid = models.CharField(db_column='LINETID', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_base_info'


class TCompilerQcom8939(models.Model):
    platform = models.CharField(max_length=40, blank=True, null=True)
    project = models.CharField(max_length=30, blank=True, null=True)
    projectpath = models.CharField(db_column='projectPath', max_length=200, blank=True, null=True)  # Field name made lowercase.
    branch = models.CharField(max_length=120, blank=True, null=True)
    types = models.CharField(max_length=40, blank=True, null=True)
    filestamp = models.CharField(db_column='fileStamp', max_length=40, blank=True, null=True)  # Field name made lowercase.
    objects = models.TextField(blank=True, null=True)
    compilerule = models.TextField(db_column='compileRule', blank=True, null=True)  # Field name made lowercase.
    javalist = models.TextField(db_column='javaList', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_compiler_qcom8939'


class TConfigType(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='USER_ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    functionid = models.CharField(db_column='FUNCTIONID', max_length=10, blank=True, null=True)  # Field name made lowercase.
    configtype = models.CharField(db_column='CONFIGTYPE', max_length=10, blank=True, null=True)  # Field name made lowercase.
    project_id = models.CharField(db_column='PROJECT_ID', max_length=10, blank=True, null=True)  # Field name made lowercase.
    apkid = models.CharField(db_column='APKID', max_length=40, blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='TYPE', max_length=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_config_type'


class TDownloadContrast(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    user_id = models.IntegerField(db_column='USER_ID', blank=True, null=True)  # Field name made lowercase.
    addrurl = models.CharField(db_column='ADDRURL', max_length=100, blank=True, null=True)  # Field name made lowercase.
    filename = models.CharField(db_column='FILENAME', max_length=40, blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='USERNAME', max_length=40, blank=True, null=True)  # Field name made lowercase.
    create_date = models.CharField(db_column='CREATE_DATE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    reference_id = models.CharField(db_column='REFERENCE_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    contrast_id = models.CharField(db_column='CONTRAST_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_download_contrast'


class TDownloadInfo(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    user_id = models.IntegerField(db_column='USER_ID', blank=True, null=True)  # Field name made lowercase.
    xml_url = models.CharField(db_column='XML_URL', max_length=100, blank=True, null=True)  # Field name made lowercase.
    xml_name = models.CharField(db_column='XML_NAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='USERNAME', max_length=40, blank=True, null=True)  # Field name made lowercase.
    create_date = models.CharField(db_column='CREATE_DATE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    tem_id = models.CharField(db_column='TEM_ID', max_length=40, blank=True, null=True)  # Field name made lowercase.
    upload_tag = models.CharField(db_column='UPLOAD_TAG', max_length=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_download_info'


class TEnumType(models.Model):
    enum_name = models.CharField(db_column='ENUM_NAME', max_length=50)  # Field name made lowercase.
    enum_value = models.CharField(db_column='ENUM_VALUE', max_length=50)  # Field name made lowercase.
    siteno = models.CharField(db_column='SITENO', max_length=50)  # Field name made lowercase.
    item_default = models.CharField(db_column='ITEM_DEFAULT', max_length=8, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_enum_type'


class TEnumValue(models.Model):
    enum_type = models.CharField(db_column='ENUM_TYPE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    item_name = models.CharField(db_column='ITEM_NAME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    item_value = models.CharField(db_column='ITEM_VALUE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    is_system = models.IntegerField(db_column='IS_SYSTEM', blank=True, null=True)  # Field name made lowercase.
    item_code = models.AutoField(db_column='ITEM_CODE', primary_key=True)  # Field name made lowercase.
    siteno = models.CharField(db_column='SITENO', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tips = models.CharField(max_length=100, blank=True, null=True)
    path = models.CharField(db_column='PATH', max_length=400, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_enum_value'


class TLog(models.Model):
    log_id = models.AutoField(db_column='LOG_ID', primary_key=True)  # Field name made lowercase.
    operate = models.CharField(db_column='OPERATE', max_length=50)  # Field name made lowercase.
    description = models.CharField(db_column='DESCRIPTION', max_length=200, blank=True, null=True)  # Field name made lowercase.
    ip = models.CharField(db_column='IP', max_length=50, blank=True, null=True)  # Field name made lowercase.
    create_by = models.CharField(db_column='CREATE_BY', max_length=50, blank=True, null=True)  # Field name made lowercase.
    create_date = models.CharField(db_column='CREATE_DATE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    functionid = models.CharField(db_column='FUNCTIONID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    project_id = models.CharField(db_column='PROJECT_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='TYPE', max_length=10, blank=True, null=True)  # Field name made lowercase.
    tem_id = models.CharField(db_column='TEM_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    siteno = models.CharField(db_column='SITENO', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_log'


class TManageCatalog(models.Model):
    catalog_id = models.AutoField(db_column='CATALOG_ID', primary_key=True)  # Field name made lowercase.
    parent_id = models.IntegerField(db_column='PARENT_ID')  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=50)  # Field name made lowercase.
    catalog_no = models.CharField(db_column='CATALOG_NO', max_length=50)  # Field name made lowercase.
    siteno = models.CharField(db_column='SITENO', max_length=50)  # Field name made lowercase.
    orderline = models.IntegerField(db_column='ORDERLINE', blank=True, null=True)  # Field name made lowercase.
    layer = models.IntegerField(db_column='LAYER', blank=True, null=True)  # Field name made lowercase.
    route = models.CharField(db_column='ROUTE', max_length=200, blank=True, null=True)  # Field name made lowercase.
    state = models.IntegerField(db_column='STATE', blank=True, null=True)  # Field name made lowercase.
    is_root = models.IntegerField(db_column='IS_ROOT', blank=True, null=True)  # Field name made lowercase.
    is_system = models.CharField(db_column='IS_SYSTEM', max_length=10, blank=True, null=True)  # Field name made lowercase.
    link_url = models.CharField(db_column='LINK_URL', max_length=255, blank=True, null=True)  # Field name made lowercase.
    small_image = models.CharField(db_column='SMALL_IMAGE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    create_by = models.CharField(db_column='CREATE_BY', max_length=50, blank=True, null=True)  # Field name made lowercase.
    create_date = models.CharField(db_column='CREATE_DATE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    modified_by = models.CharField(db_column='MODIFIED_BY', max_length=50, blank=True, null=True)  # Field name made lowercase.
    modified_date = models.CharField(db_column='MODIFIED_DATE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    childrennum = models.IntegerField(db_column='CHILDRENNUM')  # Field name made lowercase.
    description = models.CharField(db_column='DESCRIPTION', max_length=80, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_manage_catalog'


class TMobileType(models.Model):
    idx = models.AutoField(db_column='IDX', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=150, blank=True, null=True)  # Field name made lowercase.
    line_name = models.CharField(db_column='LINE_NAME', max_length=150, blank=True, null=True)  # Field name made lowercase.
    create_date = models.DateTimeField(db_column='CREATE_DATE', blank=True, null=True)  # Field name made lowercase.
    owner = models.CharField(db_column='OWNER', max_length=60, blank=True, null=True)  # Field name made lowercase.
    tid = models.IntegerField(db_column='TID', blank=True, null=True)  # Field name made lowercase.
    hardver = models.CharField(db_column='HARDVER', max_length=105, blank=True, null=True)  # Field name made lowercase.
    ucapacity = models.CharField(db_column='UCAPACITY', max_length=33, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_mobile_type'


class TPlatform(models.Model):
    platform_id = models.AutoField(db_column='PLATFORM_ID', primary_key=True)  # Field name made lowercase.
    user_id = models.IntegerField(db_column='USER_ID')  # Field name made lowercase.
    platform_name = models.CharField(db_column='PLATFORM_NAME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    platform_ver = models.CharField(db_column='PLATFORM_VER', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_platform'


class TPlm(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    url = models.TextField(db_column='URL', blank=True, null=True)  # Field name made lowercase.
    flag = models.CharField(db_column='FLAG', max_length=135, blank=True, null=True)  # Field name made lowercase.
    tips = models.CharField(db_column='TIPS', max_length=135, blank=True, null=True)  # Field name made lowercase.
    insert_time = models.DateTimeField(db_column='INSERT_TIME', blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='TYPE', max_length=10, blank=True, null=True)  # Field name made lowercase.
    change_id = models.CharField(db_column='CHANGE_ID', unique=True, max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_plm'


class TProjectInfo(models.Model):
    idx = models.AutoField()
    user_id = models.IntegerField(blank=True, null=True)
    fmw_url = models.CharField(max_length=356, blank=True, null=True)
    scm_name = models.CharField(max_length=20, blank=True, null=True)
    chip_id = models.CharField(max_length=10, blank=True, null=True)
    soft_name = models.CharField(max_length=20, blank=True, null=True)
    android_version = models.CharField(max_length=50, blank=True, null=True)
    project_id = models.CharField(max_length=10, blank=True, null=True)
    rom_version = models.CharField(max_length=128)
    tips = models.TextField(blank=True, null=True)
    platform_id = models.CharField(max_length=10, blank=True, null=True)
    market_type = models.CharField(max_length=10, blank=True, null=True)
    platform = models.CharField(max_length=50, blank=True, null=True)
    chip = models.CharField(max_length=50, blank=True, null=True)
    project = models.CharField(max_length=50, blank=True, null=True)
    servicer_name = models.CharField(max_length=300, blank=True, null=True)
    config_type = models.CharField(max_length=10, blank=True, null=True)
    external_release_name = models.CharField(max_length=30, blank=True, null=True)
    external_name = models.CharField(max_length=30, blank=True, null=True)
    vivosdk_option = models.CharField(max_length=30, blank=True, null=True)
    android_budilid = models.CharField(max_length=200, blank=True, null=True)
    displaysize = models.CharField(max_length=30, blank=True, null=True)
    screen_resolution = models.CharField(max_length=30, blank=True, null=True)
    romsize = models.CharField(max_length=30, blank=True, null=True)
    compile_option = models.CharField(max_length=30, blank=True, null=True)
    dmssid = models.CharField(max_length=80, blank=True, null=True)
    amssid = models.CharField(max_length=80, blank=True, null=True)
    driver_name = models.CharField(max_length=20, blank=True, null=True)
    system_engineer = models.CharField(max_length=20, blank=True, null=True)
    start_time = models.CharField(max_length=30, blank=True, null=True)
    finished_time = models.CharField(max_length=30, blank=True, null=True)
    network_type = models.CharField(max_length=500, blank=True, null=True)
    module_engineer = models.CharField(max_length=1000, blank=True, null=True)
    ramsize = models.CharField(max_length=30, blank=True, null=True)
    frontcamera = models.CharField(max_length=50, blank=True, null=True)
    maincamera = models.CharField(max_length=50, blank=True, null=True)
    batterycapacity = models.CharField(max_length=20, blank=True, null=True)
    networkmodel = models.CharField(max_length=50, blank=True, null=True)
    phonecolor = models.CharField(max_length=100, blank=True, null=True)
    tfsupport = models.CharField(max_length=6, blank=True, null=True)
    tfmaxsize = models.CharField(max_length=30, blank=True, null=True)
    phonenewfunction = models.CharField(max_length=100, blank=True, null=True)
    newdevice = models.CharField(max_length=100, blank=True, null=True)
    hardwareversion = models.CharField(db_column='hardwareVersion', max_length=30, blank=True, null=True)  # Field name made lowercase.
    voiceschemes = models.CharField(max_length=50, blank=True, null=True)
    functionset = models.CharField(max_length=100, blank=True, null=True)
    romstyle = models.CharField(max_length=50, blank=True, null=True)
    supportarea = models.CharField(max_length=200, blank=True, null=True)
    bspbranch = models.CharField(max_length=400, blank=True, null=True)
    sqa = models.CharField(max_length=50, blank=True, null=True)
    complaints = models.CharField(max_length=50, blank=True, null=True)
    projectstate = models.CharField(max_length=5, blank=True, null=True)
    resolution = models.CharField(max_length=20, blank=True, null=True)
    density = models.CharField(max_length=50, blank=True, null=True)
    productiondate = models.CharField(db_column='productionDate', max_length=50, blank=True, null=True)  # Field name made lowercase.
    remark = models.CharField(max_length=500, blank=True, null=True)
    cpu = models.CharField(max_length=200, blank=True, null=True)
    basicfrequency = models.CharField(max_length=200, blank=True, null=True)
    cardtype = models.CharField(db_column='cardType', max_length=10, blank=True, null=True)  # Field name made lowercase.
    sensors = models.CharField(max_length=100, blank=True, null=True)
    wcn = models.CharField(max_length=100, blank=True, null=True)
    exportdivisiontable = models.CharField(max_length=300, blank=True, null=True)
    domesticdivisiontable = models.CharField(max_length=300, blank=True, null=True)
    willstart = models.CharField(max_length=500, blank=True, null=True)
    plan = models.CharField(max_length=300, blank=True, null=True)
    phoneallocationtable = models.CharField(max_length=300, blank=True, null=True)
    projectinfotable = models.CharField(max_length=300, blank=True, null=True)
    projectnode = models.CharField(max_length=300, blank=True, null=True)
    othermember = models.CharField(db_column='otherMember', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    codeversion = models.CharField(max_length=100, blank=True, null=True)
    codepath = models.CharField(max_length=300, blank=True, null=True)
    branchinfofile = models.CharField(max_length=300, blank=True, null=True)
    configname = models.CharField(max_length=300, blank=True, null=True)
    configtable = models.CharField(max_length=300, blank=True, null=True)
    allupdatetable = models.CharField(max_length=300, blank=True, null=True)
    reviewpermissions = models.CharField(max_length=300, blank=True, null=True)
    mppath = models.CharField(max_length=200, blank=True, null=True)
    appath = models.CharField(max_length=200, blank=True, null=True)
    rsync_des = models.CharField(max_length=50)
    unifiedproject = models.CharField(db_column='unifiedProject', max_length=50, blank=True, null=True)  # Field name made lowercase.
    initprojectdate = models.CharField(db_column='initProjectDate', max_length=20, blank=True, null=True)  # Field name made lowercase.
    batterytype = models.CharField(db_column='batteryType', max_length=4, blank=True, null=True)  # Field name made lowercase.
    simtype = models.CharField(db_column='simType', max_length=4, blank=True, null=True)  # Field name made lowercase.
    volte_type = models.CharField(max_length=6, blank=True, null=True)
    encoding_voice = models.CharField(max_length=30, blank=True, null=True)
    software_qa = models.CharField(max_length=30, blank=True, null=True)
    software_sse = models.CharField(max_length=30, blank=True, null=True)
    nowprojectstate = models.CharField(max_length=4, blank=True, null=True)
    shortlisted = models.CharField(max_length=20, blank=True, null=True)
    publishcode = models.CharField(db_column='publishCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    softwareleader = models.CharField(db_column='softwareLeader', max_length=20, blank=True, null=True)  # Field name made lowercase.
    configurename = models.CharField(db_column='configureName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    secrecytype = models.CharField(db_column='secrecyType', max_length=4, blank=True, null=True)  # Field name made lowercase.
    cncdate = models.CharField(db_column='cncDate', max_length=20, blank=True, null=True)  # Field name made lowercase.
    testmolddate = models.CharField(db_column='testMoldDate', max_length=20, blank=True, null=True)  # Field name made lowercase.
    pilotdate = models.CharField(db_column='pilotDate', max_length=20, blank=True, null=True)  # Field name made lowercase.
    pilotclosedloopdate = models.CharField(db_column='pilotClosedLoopDate', max_length=20, blank=True, null=True)  # Field name made lowercase.
    batchproductiondate = models.CharField(db_column='batchProductionDate', max_length=20, blank=True, null=True)  # Field name made lowercase.
    shortlistedtestdate = models.CharField(db_column='shortListedTestDate', max_length=20, blank=True, null=True)  # Field name made lowercase.
    firstproductiondate = models.CharField(db_column='firstProductionDate', max_length=20, blank=True, null=True)  # Field name made lowercase.
    bugenddate = models.CharField(db_column='bugEndDate', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_project_info'
        unique_together = (('idx', 'rom_version'),)


class TRole(models.Model):
    role_id = models.AutoField(db_column='ROLE_ID', primary_key=True)  # Field name made lowercase.
    roleno = models.CharField(db_column='ROLENO', max_length=50, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    siteno = models.CharField(db_column='SITENO', max_length=50, blank=True, null=True)  # Field name made lowercase.
    is_system = models.CharField(db_column='IS_SYSTEM', max_length=20, blank=True, null=True)  # Field name made lowercase.
    create_by = models.CharField(db_column='CREATE_BY', max_length=50, blank=True, null=True)  # Field name made lowercase.
    create_date = models.CharField(db_column='CREATE_DATE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    modified_by = models.CharField(db_column='MODIFIED_BY', max_length=50, blank=True, null=True)  # Field name made lowercase.
    modified_date = models.CharField(db_column='MODIFIED_DATE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='DESCRIPTION', max_length=255, blank=True, null=True)  # Field name made lowercase.
    catalog_id = models.IntegerField(db_column='CATALOG_ID', blank=True, null=True)  # Field name made lowercase.
    parent_id = models.CharField(db_column='PARENT_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    route = models.CharField(db_column='ROUTE', max_length=200, blank=True, null=True)  # Field name made lowercase.
    link_url = models.CharField(db_column='LINK_URL', max_length=255, blank=True, null=True)  # Field name made lowercase.
    childrennum = models.IntegerField(db_column='CHILDRENNUM', blank=True, null=True)  # Field name made lowercase.
    chargeman = models.CharField(db_column='CHARGEMAN', max_length=10, blank=True, null=True)  # Field name made lowercase.
    minister = models.CharField(db_column='MINISTER', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_role'


class TRoleCatalogRight(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    role_id = models.IntegerField(db_column='ROLE_ID')  # Field name made lowercase.
    type = models.IntegerField(db_column='TYPE', blank=True, null=True)  # Field name made lowercase.
    catalog_id_list = models.TextField(db_column='CATALOG_ID_LIST', blank=True, null=True)  # Field name made lowercase.
    siteno = models.CharField(db_column='SITENO', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_role_catalog_right'


class TRoleFunctionInfo(models.Model):
    user_id = models.IntegerField(db_column='USER_ID')  # Field name made lowercase.
    role_id = models.CharField(db_column='ROLE_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    function_id = models.TextField(db_column='FUNCTION_ID', blank=True, null=True)  # Field name made lowercase.
    newdate = models.CharField(db_column='NEWDATE', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_role_function_info'


class TRoleRight(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    role_id = models.IntegerField(db_column='ROLE_ID')  # Field name made lowercase.
    catalog_no_list = models.CharField(db_column='CATALOG_NO_LIST', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    siteno = models.CharField(db_column='SITENO', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_role_right'


class TRoleSiteRight(models.Model):
    id = models.IntegerField(db_column='ID')  # Field name made lowercase.
    role_id = models.IntegerField(db_column='ROLE_ID')  # Field name made lowercase.
    site_no_list = models.CharField(db_column='SITE_NO_LIST', max_length=400, blank=True, null=True)  # Field name made lowercase.
    siteno = models.CharField(db_column='SITENO', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_role_site_right'


class TRoleUser(models.Model):
    role_id = models.IntegerField(db_column='ROLE_ID')  # Field name made lowercase.
    user_id = models.IntegerField(db_column='USER_ID')  # Field name made lowercase.
    siteno = models.CharField(db_column='SITENO', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_role_user'


class TSctest002(models.Model):
    id = models.CharField(db_column='ID', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_sctest002'


class TSctest003(models.Model):
    id = models.CharField(db_column='ID', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_sctest003'


class TServerMachine(models.Model):
    machine_id = models.AutoField(primary_key=True)
    host_ip = models.CharField(max_length=50, blank=True, null=True)
    hostname = models.CharField(max_length=50, blank=True, null=True)
    owner = models.CharField(max_length=50, blank=True, null=True)
    username = models.CharField(max_length=50, blank=True, null=True)
    password = models.CharField(max_length=50, blank=True, null=True)
    svnshcpermit = models.CharField(max_length=50, blank=True, null=True)
    information = models.CharField(max_length=250, blank=True, null=True)
    brand = models.CharField(max_length=50, blank=True, null=True)
    location = models.CharField(max_length=50, blank=True, null=True)
    mac_addr = models.CharField(max_length=50, blank=True, null=True)
    asset_tag = models.CharField(max_length=50, blank=True, null=True)
    userlist = models.CharField(max_length=50, blank=True, null=True)
    shared_nfs = models.CharField(max_length=50, blank=True, null=True)
    shared_smb = models.CharField(max_length=50, blank=True, null=True)
    command = models.CharField(max_length=50, blank=True, null=True)
    reg_time = models.CharField(max_length=50, blank=True, null=True)
    flag = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_server_machine'


class TSite(models.Model):
    id = models.IntegerField(db_column='ID')  # Field name made lowercase.
    siteno = models.CharField(db_column='SITENO', max_length=50)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=50)  # Field name made lowercase.
    state = models.IntegerField(db_column='STATE')  # Field name made lowercase.
    is_main = models.IntegerField(db_column='IS_MAIN')  # Field name made lowercase.
    publish_path = models.CharField(db_column='PUBLISH_PATH', max_length=255, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='DESCRIPTION', max_length=200, blank=True, null=True)  # Field name made lowercase.
    create_by = models.CharField(db_column='CREATE_BY', max_length=50, blank=True, null=True)  # Field name made lowercase.
    create_date = models.CharField(db_column='CREATE_DATE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    modified_by = models.CharField(db_column='MODIFIED_BY', max_length=50, blank=True, null=True)  # Field name made lowercase.
    modified_date = models.CharField(db_column='MODIFIED_DATE', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_site'


class TSourcecodeInfo(models.Model):
    code_id = models.AutoField(db_column='CODE_ID', primary_key=True)  # Field name made lowercase.
    codepath = models.CharField(db_column='CODEPATH', max_length=400, blank=True, null=True)  # Field name made lowercase.
    codeversion = models.CharField(db_column='CODEVERSION', max_length=100, blank=True, null=True)  # Field name made lowercase.
    branchpath = models.CharField(db_column='BRANCHPATH', max_length=400, blank=True, null=True)  # Field name made lowercase.
    meanline = models.CharField(db_column='MEANLINE', max_length=400, blank=True, null=True)  # Field name made lowercase.
    productionline = models.CharField(db_column='PRODUCTIONLINE', max_length=400, blank=True, null=True)  # Field name made lowercase.
    productline = models.CharField(db_column='PRODUCTLINE', max_length=400, blank=True, null=True)  # Field name made lowercase.
    userid = models.IntegerField(db_column='USERID', blank=True, null=True)  # Field name made lowercase.
    apktype = models.CharField(db_column='APKTYPE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    functionid = models.CharField(db_column='FUNCTIONID', max_length=400, blank=True, null=True)  # Field name made lowercase.
    project_name = models.CharField(db_column='PROJECT_NAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    project_id = models.CharField(db_column='PROJECT_ID', max_length=40, blank=True, null=True)  # Field name made lowercase.
    configdate = models.CharField(db_column='CONFIGDATE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='USERNAME', max_length=30, blank=True, null=True)  # Field name made lowercase.
    remark = models.CharField(db_column='REMARK', max_length=400, blank=True, null=True)  # Field name made lowercase.
    newdate = models.CharField(db_column='NEWDATE', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_sourcecode_info'


class TSourcecodeTemplateInfo(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    code_id = models.IntegerField(db_column='CODE_ID', blank=True, null=True)  # Field name made lowercase.
    codepath = models.CharField(db_column='CODEPATH', max_length=400, blank=True, null=True)  # Field name made lowercase.
    codeversion = models.CharField(db_column='CODEVERSION', max_length=100, blank=True, null=True)  # Field name made lowercase.
    branchpath = models.CharField(db_column='BRANCHPATH', max_length=400, blank=True, null=True)  # Field name made lowercase.
    meanline = models.CharField(db_column='MEANLINE', max_length=400, blank=True, null=True)  # Field name made lowercase.
    productionline = models.CharField(db_column='PRODUCTIONLINE', max_length=400, blank=True, null=True)  # Field name made lowercase.
    productline = models.CharField(db_column='PRODUCTLINE', max_length=400, blank=True, null=True)  # Field name made lowercase.
    userid = models.IntegerField(db_column='USERID', blank=True, null=True)  # Field name made lowercase.
    apktype = models.CharField(db_column='APKTYPE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    functionid = models.CharField(db_column='FUNCTIONID', max_length=400, blank=True, null=True)  # Field name made lowercase.
    project_name = models.CharField(db_column='PROJECT_NAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    project_id = models.CharField(db_column='PROJECT_ID', max_length=40, blank=True, null=True)  # Field name made lowercase.
    newdate = models.CharField(db_column='NEWDATE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    tem_id = models.CharField(db_column='TEM_ID', max_length=200, blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='USERNAME', max_length=30, blank=True, null=True)  # Field name made lowercase.
    remark = models.CharField(db_column='REMARK', max_length=400, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_sourcecode_template_info'


class TStatus(models.Model):
    tid = models.IntegerField(db_column='TID', blank=True, null=True)  # Field name made lowercase.
    urar_status = models.CharField(db_column='URAR_STATUS', max_length=45, blank=True, null=True)  # Field name made lowercase.
    rsync_status = models.CharField(db_column='RSYNC_STATUS', max_length=45, blank=True, null=True)  # Field name made lowercase.
    plm_status = models.TextField(db_column='PLM_STATUS', blank=True, null=True)  # Field name made lowercase.
    parse_url_status = models.CharField(db_column='PARSE_URL_STATUS', max_length=45, blank=True, null=True)  # Field name made lowercase.
    insert_upload_status = models.CharField(db_column='INSERT_UPLOAD_STATUS', max_length=10, blank=True, null=True)  # Field name made lowercase.
    tag = models.TextField(db_column='TAG', blank=True, null=True)  # Field name made lowercase.
    createddate = models.CharField(db_column='CREATEDDATE', max_length=40)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_status'


class TTemplateIdentifying(models.Model):
    tem_id = models.AutoField(db_column='TEM_ID', primary_key=True)  # Field name made lowercase.
    tem_version = models.CharField(db_column='TEM_VERSION', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tem_date = models.CharField(db_column='TEM_DATE', max_length=40, blank=True, null=True)  # Field name made lowercase.
    project_id = models.CharField(db_column='PROJECT_ID', max_length=40, blank=True, null=True)  # Field name made lowercase.
    temtype = models.CharField(db_column='TEMTYPE', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_template_identifying'


class TTest(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    apk_id = models.IntegerField(blank=True, null=True)
    code_id = models.CharField(max_length=400, blank=True, null=True)
    functionid = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_test'


class TTest1(models.Model):
    apk_id = models.AutoField(db_column='APK_ID', primary_key=True)  # Field name made lowercase.
    apkversion = models.CharField(db_column='APKVERSION', max_length=100, blank=True, null=True)  # Field name made lowercase.
    apkpath = models.CharField(db_column='APKPATH', max_length=400, blank=True, null=True)  # Field name made lowercase.
    platform = models.CharField(db_column='PLATFORM', max_length=400, blank=True, null=True)  # Field name made lowercase.
    heirname = models.CharField(db_column='HEIRNAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    apkname = models.CharField(db_column='APKNAME', max_length=300, blank=True, null=True)  # Field name made lowercase.
    filepath = models.CharField(db_column='FILEPATH', max_length=400, blank=True, null=True)  # Field name made lowercase.
    newdate = models.CharField(db_column='NEWDATE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    encrypt = models.CharField(db_column='ENCRYPT', max_length=100, blank=True, null=True)  # Field name made lowercase.
    userid = models.IntegerField(db_column='USERID', blank=True, null=True)  # Field name made lowercase.
    apktype = models.CharField(db_column='APKTYPE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    functionid = models.CharField(db_column='FUNCTIONID', max_length=400, blank=True, null=True)  # Field name made lowercase.
    project_name = models.CharField(db_column='PROJECT_NAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    project_id = models.CharField(db_column='PROJECT_ID', max_length=40, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_test1'


class TUploadInfo(models.Model):
    tid = models.AutoField(db_column='TID', primary_key=True)  # Field name made lowercase.
    model = models.CharField(db_column='MODEL', max_length=150, blank=True, null=True)  # Field name made lowercase.
    modeltype = models.IntegerField(db_column='MODELTYPE', blank=True, null=True)  # Field name made lowercase.
    line_name = models.CharField(db_column='LINE_NAME', max_length=150, blank=True, null=True)  # Field name made lowercase.
    tfdata_rar = models.TextField(db_column='TFDATA_RAR', blank=True, null=True)  # Field name made lowercase.
    third_party_zip = models.CharField(db_column='THIRD_PARTY_ZIP', max_length=768, blank=True, null=True)  # Field name made lowercase.
    tools_zip = models.CharField(db_column='TOOLS_ZIP', max_length=768, blank=True, null=True)  # Field name made lowercase.
    tf_img_zip = models.CharField(db_column='TF_IMG_ZIP', max_length=768, blank=True, null=True)  # Field name made lowercase.
    tf_full_zip = models.CharField(db_column='TF_FULL_ZIP', max_length=768, blank=True, null=True)  # Field name made lowercase.
    md5_txt = models.TextField(db_column='MD5_TXT', blank=True, null=True)  # Field name made lowercase.
    upload_type = models.CharField(db_column='UPLOAD_TYPE', max_length=15, blank=True, null=True)  # Field name made lowercase.
    urar_status = models.CharField(db_column='URAR_STATUS', max_length=15, blank=True, null=True)  # Field name made lowercase.
    rsync_status = models.CharField(db_column='RSYNC_STATUS', max_length=15, blank=True, null=True)  # Field name made lowercase.
    third_yd_zip = models.CharField(db_column='THIRD_YD_ZIP', max_length=768, blank=True, null=True)  # Field name made lowercase.
    json = models.CharField(db_column='JSON', max_length=768, blank=True, null=True)  # Field name made lowercase.
    updatestatus = models.CharField(db_column='UPDATESTATUS', max_length=12, blank=True, null=True)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CREATEDDATE', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CREATEDBY', max_length=60, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_upload_info'


class TUser(models.Model):
    user_id = models.AutoField(db_column='USER_ID', primary_key=True)  # Field name made lowercase.
    siteno = models.CharField(db_column='SITENO', max_length=50, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(db_column='PASSWORD', max_length=50, blank=True, null=True)  # Field name made lowercase.
    state = models.IntegerField(db_column='STATE', blank=True, null=True)  # Field name made lowercase.
    is_system = models.IntegerField(db_column='IS_SYSTEM', blank=True, null=True)  # Field name made lowercase.
    login_times = models.IntegerField(db_column='LOGIN_TIMES', blank=True, null=True)  # Field name made lowercase.
    last_time = models.CharField(db_column='LAST_TIME', max_length=20, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='EMAIL', max_length=50, blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(db_column='PHONE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mobile = models.CharField(db_column='MOBILE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    create_by = models.CharField(db_column='CREATE_BY', max_length=50, blank=True, null=True)  # Field name made lowercase.
    create_date = models.CharField(db_column='CREATE_DATE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    modified_by = models.CharField(db_column='MODIFIED_BY', max_length=50, blank=True, null=True)  # Field name made lowercase.
    modified_date = models.CharField(db_column='MODIFIED_DATE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    uid2 = models.CharField(db_column='UID2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sitename = models.CharField(db_column='SITENAME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    functionid = models.CharField(db_column='FUNCTIONID', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    functionname = models.TextField(db_column='FUNCTIONNAME', blank=True, null=True)  # Field name made lowercase.
    branchid = models.CharField(db_column='BRANCHID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    branchname = models.CharField(db_column='BRANCHNAME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    function_state = models.CharField(db_column='FUNCTION_STATE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    twicefunctionid = models.TextField(db_column='TWICEFUNCTIONID', blank=True, null=True)  # Field name made lowercase.
    twicefunctionname = models.TextField(db_column='TWICEFUNCTIONNAME', blank=True, null=True)  # Field name made lowercase.
    twiceallfunctionid = models.TextField(db_column='TWICEALLFUNCTIONID', blank=True, null=True)  # Field name made lowercase.
    twicefunctionstate = models.CharField(db_column='TWICEFUNCTIONSTATE', max_length=10, blank=True, null=True)  # Field name made lowercase.
    twiceallfunctionname = models.TextField(db_column='TWICEALLFUNCTIONNAME', blank=True, null=True)  # Field name made lowercase.
    emailstate = models.CharField(db_column='EMAILSTATE', max_length=10, blank=True, null=True)  # Field name made lowercase.
    operationtype = models.CharField(db_column='OPERATIONTYPE', max_length=10, blank=True, null=True)  # Field name made lowercase.
    treeedittype = models.CharField(db_column='TREEEDITTYPE', max_length=4, blank=True, null=True)  # Field name made lowercase.
    idcode = models.CharField(db_column='IDCODE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    department = models.CharField(db_column='DEPARTMENT', max_length=100, blank=True, null=True)  # Field name made lowercase.
    oacode = models.CharField(db_column='OACODE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='TYPE', max_length=4, blank=True, null=True)  # Field name made lowercase.
    chargeman = models.CharField(db_column='CHARGEMAN', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_user'


class TVivoBaseline(models.Model):
    function_id = models.CharField(max_length=50, blank=True, null=True)
    function_name = models.CharField(max_length=30, blank=True, null=True)
    sdk_type = models.CharField(max_length=4, blank=True, null=True)
    base_line_type = models.CharField(max_length=4, blank=True, null=True)
    sdk_level = models.CharField(max_length=30, blank=True, null=True)
    test_person_name = models.CharField(max_length=200, blank=True, null=True)
    base_branch = models.CharField(max_length=500, blank=True, null=True)
    function_person_name = models.CharField(max_length=200, blank=True, null=True)
    config_date = models.CharField(max_length=30, blank=True, null=True)
    create_name = models.CharField(max_length=10, blank=True, null=True)
    create_id = models.CharField(max_length=10, blank=True, null=True)
    project_id = models.CharField(max_length=10, blank=True, null=True)
    project_name = models.CharField(max_length=20, blank=True, null=True)
    group_id = models.CharField(max_length=10, blank=True, null=True)
    group_name = models.CharField(max_length=30, blank=True, null=True)
    branch_id = models.CharField(max_length=10, blank=True, null=True)
    branch_name = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_vivo_baseline'


class TVivoBaselineConfig(models.Model):
    function_id = models.CharField(max_length=50, blank=True, null=True)
    function_name = models.CharField(max_length=30, blank=True, null=True)
    sdk_type = models.CharField(max_length=4, blank=True, null=True)
    base_line_type = models.CharField(max_length=4, blank=True, null=True)
    sdk_level = models.CharField(max_length=30, blank=True, null=True)
    test_person_name = models.CharField(max_length=200, blank=True, null=True)
    base_line_branch = models.CharField(max_length=500, blank=True, null=True)
    function_person_name = models.CharField(max_length=200, blank=True, null=True)
    config_date = models.CharField(max_length=30, blank=True, null=True)
    create_name = models.CharField(max_length=10, blank=True, null=True)
    create_id = models.CharField(max_length=10, blank=True, null=True)
    project_id = models.CharField(max_length=10, blank=True, null=True)
    project_name = models.CharField(max_length=20, blank=True, null=True)
    mean_line = models.CharField(max_length=300, blank=True, null=True)
    product_line = models.CharField(max_length=300, blank=True, null=True)
    code_path = models.CharField(max_length=100, blank=True, null=True)
    base_line_id = models.CharField(max_length=30, blank=True, null=True)
    create_date = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_vivo_baseline_config'


class TVivoBaselineProject(models.Model):
    function_id = models.CharField(max_length=50, blank=True, null=True)
    config_id = models.CharField(max_length=4, blank=True, null=True)
    config_date = models.CharField(max_length=30, blank=True, null=True)
    create_id = models.CharField(max_length=10, blank=True, null=True)
    project_id = models.CharField(max_length=10, blank=True, null=True)
    project_name = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_vivo_baseline_project'


class TVivoBranchHistory(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    function = models.CharField(db_column='FUNCTION', max_length=300, blank=True, null=True)  # Field name made lowercase.
    branch = models.CharField(db_column='BRANCH', max_length=100, blank=True, null=True)  # Field name made lowercase.
    project = models.CharField(db_column='PROJECT', max_length=30, blank=True, null=True)  # Field name made lowercase.
    xml_name = models.CharField(db_column='XML_NAME', max_length=300, blank=True, null=True)  # Field name made lowercase.
    xml_date = models.CharField(db_column='XML_DATE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    branch_type = models.CharField(db_column='BRANCH_TYPE', max_length=10, blank=True, null=True)  # Field name made lowercase.
    config_name = models.CharField(db_column='CONFIG_NAME', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_vivo_branch_history'


class TVivoBugState(models.Model):
    project = models.CharField(max_length=30, blank=True, null=True)
    version = models.CharField(max_length=30, blank=True, null=True)
    svnpath = models.CharField(db_column='svnPath', max_length=300, blank=True, null=True)  # Field name made lowercase.
    manifestpath = models.CharField(db_column='manifestPath', max_length=300, blank=True, null=True)  # Field name made lowercase.
    encrypt_size = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=4, blank=True, null=True)
    user_id = models.CharField(max_length=30, blank=True, null=True)
    create_by = models.CharField(max_length=30, blank=True, null=True)
    create_date = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_vivo_bug_state'


class TVivoBuginfo(models.Model):
    project = models.CharField(max_length=30, blank=True, null=True)
    hdversion = models.CharField(max_length=30, blank=True, null=True)
    bugid = models.CharField(max_length=100, blank=True, null=True)
    commitinfo = models.TextField(blank=True, null=True)
    create_by = models.CharField(max_length=30, blank=True, null=True)
    create_date = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_vivo_buginfo'


class TVivoCarrierType(models.Model):
    project = models.CharField(max_length=30, blank=True, null=True)
    project_id = models.CharField(max_length=20, blank=True, null=True)
    carrier_info = models.CharField(max_length=200, blank=True, null=True)
    carrier_id = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_vivo_carrier_type'


class TVivoCompiler(models.Model):
    compiledate = models.DateTimeField(db_column='compileDate')  # Field name made lowercase.
    platform = models.CharField(max_length=20, blank=True, null=True)
    project = models.CharField(max_length=30, blank=True, null=True)
    softwareversion = models.CharField(db_column='softwareVersion', max_length=500, blank=True, null=True)  # Field name made lowercase.
    compiletype = models.CharField(db_column='compileType', max_length=30, blank=True, null=True)  # Field name made lowercase.
    softwaretype = models.CharField(db_column='softwareType', max_length=20, blank=True, null=True)  # Field name made lowercase.
    issystemsoftware = models.CharField(db_column='isSystemSoftware', max_length=20, blank=True, null=True)  # Field name made lowercase.
    onlinetype = models.CharField(db_column='onlineType', max_length=20, blank=True, null=True)  # Field name made lowercase.
    configurename = models.CharField(db_column='configureName', max_length=30, blank=True, null=True)  # Field name made lowercase.
    softwareleader = models.CharField(db_column='softwareLeader', max_length=20, blank=True, null=True)  # Field name made lowercase.
    compiletime = models.CharField(db_column='compileTime', max_length=20, blank=True, null=True)  # Field name made lowercase.
    compileserver = models.CharField(db_column='compileServer', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_vivo_compiler'


class TVivoCustomerService(models.Model):
    tid = models.AutoField(db_column='TID', primary_key=True)  # Field name made lowercase.
    model = models.CharField(db_column='MODEL', max_length=150, blank=True, null=True)  # Field name made lowercase.
    modeltype = models.IntegerField(db_column='MODELTYPE', blank=True, null=True)  # Field name made lowercase.
    line_name = models.CharField(db_column='LINE_NAME', max_length=150, blank=True, null=True)  # Field name made lowercase.
    tfdata_rar = models.TextField(db_column='TFDATA_RAR', blank=True, null=True)  # Field name made lowercase.
    third_party_zip = models.CharField(db_column='THIRD_PARTY_ZIP', max_length=768, blank=True, null=True)  # Field name made lowercase.
    tools_zip = models.CharField(db_column='TOOLS_ZIP', max_length=768, blank=True, null=True)  # Field name made lowercase.
    tf_img_zip = models.CharField(db_column='TF_IMG_ZIP', max_length=768, blank=True, null=True)  # Field name made lowercase.
    tf_full_zip = models.CharField(db_column='TF_FULL_ZIP', max_length=768, blank=True, null=True)  # Field name made lowercase.
    md5_txt = models.TextField(db_column='MD5_TXT', blank=True, null=True)  # Field name made lowercase.
    upload_type = models.CharField(db_column='UPLOAD_TYPE', max_length=15, blank=True, null=True)  # Field name made lowercase.
    urar_status = models.CharField(db_column='URAR_STATUS', max_length=15, blank=True, null=True)  # Field name made lowercase.
    rsync_status = models.CharField(db_column='RSYNC_STATUS', max_length=15, blank=True, null=True)  # Field name made lowercase.
    third_yd_zip = models.CharField(db_column='THIRD_YD_ZIP', max_length=768, blank=True, null=True)  # Field name made lowercase.
    json = models.CharField(db_column='JSON', max_length=768, blank=True, null=True)  # Field name made lowercase.
    updatestatus = models.CharField(db_column='UPDATESTATUS', max_length=12, blank=True, null=True)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CREATEDDATE', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CREATEDBY', max_length=60, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_vivo_customer_service'


class TVivoFunctionConfig(models.Model):
    function_id = models.AutoField(db_column='FUNCTION_ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    create_by = models.CharField(db_column='CREATE_BY', max_length=50, blank=True, null=True)  # Field name made lowercase.
    create_date = models.CharField(db_column='CREATE_DATE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    modified_by = models.CharField(db_column='MODIFIED_BY', max_length=50, blank=True, null=True)  # Field name made lowercase.
    modified_date = models.CharField(db_column='MODIFIED_DATE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='DESCRIPTION', max_length=255, blank=True, null=True)  # Field name made lowercase.
    catalog_id = models.IntegerField(db_column='CATALOG_ID', blank=True, null=True)  # Field name made lowercase.
    parent_id = models.CharField(db_column='PARENT_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    route = models.CharField(db_column='ROUTE', max_length=200, blank=True, null=True)  # Field name made lowercase.
    link_url = models.CharField(db_column='LINK_URL', max_length=255, blank=True, null=True)  # Field name made lowercase.
    childrennum = models.IntegerField(db_column='CHILDRENNUM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_vivo_function_config'


class TVivoManifest(models.Model):
    project = models.CharField(max_length=30, blank=True, null=True)
    version = models.CharField(max_length=40, blank=True, null=True)
    bugid = models.CharField(max_length=100, blank=True, null=True)
    projectpath = models.CharField(db_column='projectPath', max_length=200, blank=True, null=True)  # Field name made lowercase.
    bugbranch = models.CharField(db_column='bugBranch', max_length=90, blank=True, null=True)  # Field name made lowercase.
    lastbranch = models.CharField(db_column='lastBranch', max_length=90, blank=True, null=True)  # Field name made lowercase.
    lastcommitid = models.CharField(db_column='lastCommitId', max_length=200, blank=True, null=True)  # Field name made lowercase.
    newbranch = models.CharField(db_column='newBranch', max_length=90, blank=True, null=True)  # Field name made lowercase.
    submitid = models.CharField(db_column='submitId', max_length=90, blank=True, null=True)  # Field name made lowercase.
    managename = models.CharField(db_column='manageName', max_length=30, blank=True, null=True)  # Field name made lowercase.
    buginfo = models.TextField(db_column='bugInfo', blank=True, null=True)  # Field name made lowercase.
    reviewer = models.CharField(max_length=500, blank=True, null=True)
    owner = models.CharField(max_length=500, blank=True, null=True)
    hdversion = models.CharField(max_length=40, blank=True, null=True)
    project_id = models.CharField(max_length=20, blank=True, null=True)
    newdate = models.CharField(max_length=20, blank=True, null=True)
    lastversion = models.CharField(db_column='lastVersion', max_length=40, blank=True, null=True)  # Field name made lowercase.
    setstatus = models.CharField(db_column='setStatus', max_length=4, blank=True, null=True)  # Field name made lowercase.
    setdate = models.CharField(db_column='setDate', max_length=20, blank=True, null=True)  # Field name made lowercase.
    setuser = models.CharField(db_column='setUser', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_vivo_manifest'


class TVivoManifestContrast(models.Model):
    uid = models.CharField(max_length=40, blank=True, null=True)
    path = models.CharField(max_length=300, blank=True, null=True)
    branch1 = models.CharField(max_length=200, blank=True, null=True)
    version1 = models.CharField(max_length=200, blank=True, null=True)
    branch2 = models.CharField(max_length=200, blank=True, null=True)
    version2 = models.CharField(max_length=200, blank=True, null=True)
    updatetype = models.CharField(db_column='updateType', max_length=4, blank=True, null=True)  # Field name made lowercase.
    loginfo = models.TextField(db_column='logInfo', blank=True, null=True)  # Field name made lowercase.
    create_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 't_vivo_manifest_contrast'


class TVivoManifestLog(models.Model):
    commit_id = models.CharField(max_length=20, blank=True, null=True)
    commit_owner = models.CharField(max_length=40, blank=True, null=True)
    commit_time = models.CharField(max_length=20, blank=True, null=True)
    commit_info = models.TextField(blank=True, null=True)
    branch = models.CharField(max_length=100, blank=True, null=True)
    project = models.CharField(max_length=100, blank=True, null=True)
    commit_uuid = models.CharField(max_length=60, blank=True, null=True)
    id = models.AutoField(unique=True)

    class Meta:
        managed = False
        db_table = 't_vivo_manifest_log'


class TVivoManifestProject(models.Model):
    projectversion = models.CharField(db_column='projectVersion', max_length=50, blank=True, null=True)  # Field name made lowercase.
    project = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_vivo_manifest_project'


class TVivoOnlineInfo(models.Model):
    project = models.CharField(max_length=30, blank=True, null=True)
    version = models.CharField(max_length=50, blank=True, null=True)
    opentime = models.DateTimeField(db_column='openTime', blank=True, null=True)  # Field name made lowercase.
    userratio = models.CharField(db_column='userRatio', max_length=30, blank=True, null=True)  # Field name made lowercase.
    opentype = models.CharField(db_column='openType', max_length=50, blank=True, null=True)  # Field name made lowercase.
    remarks = models.CharField(max_length=100, blank=True, null=True)
    datatime = models.DateTimeField(blank=True, null=True)
    loc = models.CharField(max_length=30, blank=True, null=True)
    pushtype = models.IntegerField(db_column='pushType', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_vivo_online_info'


class TVivoOnlineProject(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    hdversion = models.CharField(max_length=50, blank=True, null=True)
    project = models.CharField(max_length=400, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_vivo_online_project'


class TVivoOriginalBuginfo(models.Model):
    project = models.CharField(max_length=30, blank=True, null=True)
    curversion = models.CharField(max_length=20, blank=True, null=True)
    lastversion = models.CharField(max_length=20, blank=True, null=True)
    bugtype = models.CharField(db_column='bugType', max_length=30, blank=True, null=True)  # Field name made lowercase.
    bugid = models.CharField(max_length=30, blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    priority = models.CharField(max_length=30, blank=True, null=True)
    reopentimes = models.CharField(db_column='reOpenTimes', max_length=10, blank=True, null=True)  # Field name made lowercase.
    verifycounts = models.CharField(db_column='verifyCounts', max_length=10, blank=True, null=True)  # Field name made lowercase.
    workload = models.CharField(max_length=10, blank=True, null=True)
    reporter = models.CharField(max_length=30, blank=True, null=True)
    manager = models.CharField(max_length=30, blank=True, null=True)
    createtime = models.CharField(db_column='createTime', max_length=30, blank=True, null=True)  # Field name made lowercase.
    processinginstructions = models.TextField(db_column='processingInstructions', blank=True, null=True)  # Field name made lowercase.
    closer = models.CharField(max_length=30, blank=True, null=True)
    testers = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_vivo_original_buginfo'


class TVivoProjectcodeInfo(models.Model):
    id = models.IntegerField(blank=True, null=True)
    idx = models.IntegerField(blank=True, null=True)
    bspbranch = models.CharField(max_length=1200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_vivo_projectcode_info'


class TVivoQuestionProject(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    questionid = models.IntegerField(db_column='QUESTIONID', blank=True, null=True)  # Field name made lowercase.
    createname = models.CharField(db_column='CREATENAME', max_length=40, blank=True, null=True)  # Field name made lowercase.
    createdate = models.CharField(db_column='CREATEDATE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    projectname = models.CharField(db_column='PROJECTNAME', max_length=40, blank=True, null=True)  # Field name made lowercase.
    projectid = models.CharField(db_column='PROJECTID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    softwareleader = models.CharField(db_column='SOFTWARELEADER', max_length=30, blank=True, null=True)  # Field name made lowercase.
    softwareversion = models.CharField(db_column='SOFTWAREVERSION', max_length=30, blank=True, null=True)  # Field name made lowercase.
    opendate = models.CharField(db_column='OPENDATE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    softwarestate = models.CharField(db_column='SOFTWARESTATE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    onlinetype = models.CharField(db_column='ONLINETYPE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    userratio = models.CharField(db_column='USERRATIO', max_length=30, blank=True, null=True)  # Field name made lowercase.
    errorlog = models.TextField(db_column='ERRORLOG', blank=True, null=True)  # Field name made lowercase.
    remark = models.TextField(db_column='REMARK', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_vivo_question_project'


class TVivoSchemeFunction(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=60, blank=True, null=True)  # Field name made lowercase.
    is_system = models.CharField(db_column='IS_SYSTEM', max_length=60, blank=True, null=True)  # Field name made lowercase.
    create_by = models.CharField(db_column='CREATE_BY', max_length=60, blank=True, null=True)  # Field name made lowercase.
    create_date = models.CharField(db_column='CREATE_DATE', max_length=60, blank=True, null=True)  # Field name made lowercase.
    parent_id = models.IntegerField(db_column='PARENT_ID', blank=True, null=True)  # Field name made lowercase.
    route = models.CharField(db_column='ROUTE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    link_url = models.CharField(db_column='LINK_URL', max_length=100, blank=True, null=True)  # Field name made lowercase.
    childrennum = models.IntegerField(db_column='CHILDRENNUM', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='DESCRIPTION', max_length=200, blank=True, null=True)  # Field name made lowercase.
    tag = models.IntegerField(db_column='TAG', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_vivo_scheme_function'


class TVivoSchemeMarking(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    tagname = models.CharField(db_column='TAGNAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tagpath = models.CharField(db_column='TAGPATH', max_length=500, blank=True, null=True)  # Field name made lowercase.
    project_id = models.CharField(db_column='PROJECT_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    project_name = models.CharField(db_column='PROJECT_NAME', max_length=40, blank=True, null=True)  # Field name made lowercase.
    create_name = models.CharField(db_column='CREATE_NAME', max_length=20, blank=True, null=True)  # Field name made lowercase.
    create_date = models.CharField(db_column='CREATE_DATE', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_vivo_scheme_marking'


class TVivoSchemePath(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    function_id = models.IntegerField(db_column='FUNCTION_ID', blank=True, null=True)  # Field name made lowercase.
    rom_version = models.CharField(db_column='ROM_VERSION', max_length=20, blank=True, null=True)  # Field name made lowercase.
    rom_id = models.CharField(db_column='ROM_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    path = models.CharField(db_column='PATH', max_length=800, blank=True, null=True)  # Field name made lowercase.
    create_name = models.CharField(db_column='CREATE_NAME', max_length=30, blank=True, null=True)  # Field name made lowercase.
    create_date = models.CharField(db_column='CREATE_DATE', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_vivo_scheme_path'


class TVivoSchemeProject(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    romid = models.CharField(db_column='ROMID', max_length=10, blank=True, null=True)  # Field name made lowercase.
    projectid = models.CharField(db_column='PROJECTID', max_length=30, blank=True, null=True)  # Field name made lowercase.
    functionid = models.CharField(db_column='FUNCTIONID', max_length=30, blank=True, null=True)  # Field name made lowercase.
    create_date = models.CharField(db_column='CREATE_DATE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    create_by = models.CharField(db_column='CREATE_BY', max_length=20, blank=True, null=True)  # Field name made lowercase.
    userid = models.CharField(db_column='USERID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    parent_id = models.CharField(db_column='PARENT_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_vivo_scheme_project'


class TVivoSchemeTaginfo(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    tagid = models.CharField(db_column='TAGID', max_length=30, blank=True, null=True)  # Field name made lowercase.
    tagname = models.CharField(db_column='TAGNAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tagpath = models.CharField(db_column='TAGPATH', max_length=300, blank=True, null=True)  # Field name made lowercase.
    svnpath = models.CharField(db_column='SVNPATH', max_length=300, blank=True, null=True)  # Field name made lowercase.
    romid = models.CharField(db_column='ROMID', max_length=30, blank=True, null=True)  # Field name made lowercase.
    projectid = models.CharField(db_column='PROJECTID', max_length=10, blank=True, null=True)  # Field name made lowercase.
    functionid = models.CharField(db_column='FUNCTIONID', max_length=10, blank=True, null=True)  # Field name made lowercase.
    create_name = models.CharField(db_column='CREATE_NAME', max_length=20, blank=True, null=True)  # Field name made lowercase.
    create_date = models.CharField(db_column='CREATE_DATE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    tagversion = models.CharField(db_column='TAGVERSION', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_vivo_scheme_taginfo'


class TVivoSoftwareReport(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    project = models.CharField(db_column='PROJECT', max_length=50, blank=True, null=True)  # Field name made lowercase.
    projectid = models.CharField(db_column='PROJECTID', max_length=10, blank=True, null=True)  # Field name made lowercase.
    chargeperson = models.CharField(db_column='CHARGEPERSON', max_length=100, blank=True, null=True)  # Field name made lowercase.
    relatedperson = models.CharField(db_column='RELATEDPERSON', max_length=100, blank=True, null=True)  # Field name made lowercase.
    departmentid = models.CharField(db_column='DEPARTMENTID', max_length=10, blank=True, null=True)  # Field name made lowercase.
    groupid = models.CharField(db_column='GROUPID', max_length=10, blank=True, null=True)  # Field name made lowercase.
    departmentname = models.CharField(db_column='DEPARTMENTNAME', max_length=40, blank=True, null=True)  # Field name made lowercase.
    questiontime = models.CharField(db_column='QUESTIONTIME', max_length=30, blank=True, null=True)  # Field name made lowercase.
    questionversion = models.CharField(db_column='QUESTIONVERSION', max_length=300, blank=True, null=True)  # Field name made lowercase.
    questiondescription = models.TextField(db_column='QUESTIONDESCRIPTION', blank=True, null=True)  # Field name made lowercase.
    questiondiagnosis = models.CharField(db_column='QUESTIONDIAGNOSIS', max_length=100, blank=True, null=True)  # Field name made lowercase.
    questionremark = models.TextField(db_column='QUESTIONREMARK', blank=True, null=True)  # Field name made lowercase.
    depotversion = models.CharField(db_column='DEPOTVERSION', max_length=300, blank=True, null=True)  # Field name made lowercase.
    questiontype = models.CharField(db_column='QUESTIONTYPE', max_length=4, blank=True, null=True)  # Field name made lowercase.
    notername = models.CharField(db_column='NOTERNAME', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_vivo_software_report'


class TVivoSystemconfig(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    systemvalue = models.CharField(db_column='SYSTEMVALUE', max_length=500, blank=True, null=True)  # Field name made lowercase.
    systemuse = models.CharField(db_column='SYSTEMUSE', max_length=500, blank=True, null=True)  # Field name made lowercase.
    systemstateid = models.CharField(db_column='SYSTEMSTATEID', max_length=2, blank=True, null=True)  # Field name made lowercase.
    systemstatevalue = models.CharField(db_column='SYSTEMSTATEVALUE', max_length=10, blank=True, null=True)  # Field name made lowercase.
    maintainname = models.CharField(db_column='MAINTAINNAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    mkvariable = models.CharField(db_column='MKVARIABLE', max_length=500, blank=True, null=True)  # Field name made lowercase.
    remarks = models.TextField(db_column='REMARKS', blank=True, null=True)  # Field name made lowercase.
    usages = models.TextField(db_column='USAGES', blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='USERNAME', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_vivo_systemconfig'


class TVivoTest(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    project = models.CharField(max_length=100, blank=True, null=True)
    version = models.CharField(max_length=400, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_vivo_test'


class TVivoUser(models.Model):
    oacode = models.CharField(db_column='OACODE', max_length=80, blank=True, null=True)  # Field name made lowercase.
    idcode = models.CharField(db_column='IDCODE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='EMAIL', max_length=50, blank=True, null=True)  # Field name made lowercase.
    department = models.CharField(db_column='DEPARTMENT', max_length=100, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=80, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_vivo_user'


class TVivoUserCode(models.Model):
    projectid = models.IntegerField(blank=True, null=True)
    qa_id = models.CharField(max_length=30, blank=True, null=True)
    qa_name = models.CharField(max_length=30, blank=True, null=True)
    sse_id = models.CharField(max_length=30, blank=True, null=True)
    sse_name = models.CharField(max_length=30, blank=True, null=True)
    soft_id = models.CharField(max_length=30, blank=True, null=True)
    soft_name = models.CharField(max_length=30, blank=True, null=True)
    sqa_id = models.CharField(max_length=30, blank=True, null=True)
    sqa_name = models.CharField(max_length=30, blank=True, null=True)
    projectstatus = models.CharField(db_column='projectStatus', max_length=30, blank=True, null=True)  # Field name made lowercase.
    projectname = models.CharField(db_column='projectName', max_length=30, blank=True, null=True)  # Field name made lowercase.
    developstatus = models.CharField(db_column='developStatus', max_length=4, blank=True, null=True)  # Field name made lowercase.
    romversion = models.CharField(db_column='romVersion', max_length=20, blank=True, null=True)  # Field name made lowercase.
    salestype = models.CharField(db_column='salesType', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_vivo_user_code'


class TWechatInfo(models.Model):
    imei = models.CharField(db_column='IMEI', primary_key=True, max_length=20)  # Field name made lowercase.
    public_key = models.TextField(db_column='PUBLIC_KEY', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_wechat_info'


class TWechatPay(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    uniqid = models.CharField(db_column='UNIQID', max_length=100, blank=True, null=True)  # Field name made lowercase.
    pcb = models.CharField(db_column='PCB', max_length=400, blank=True, null=True)  # Field name made lowercase.
    cpuid = models.CharField(db_column='CPUID', max_length=400, blank=True, null=True)  # Field name made lowercase.
    emmcid = models.CharField(db_column='EMMCID', max_length=100, blank=True, null=True)  # Field name made lowercase.
    publickey = models.CharField(db_column='PUBLICKEY', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    filepath = models.CharField(db_column='FILEPATH', max_length=400, blank=True, null=True)  # Field name made lowercase.
    project_name = models.CharField(db_column='PROJECT_NAME', max_length=200, blank=True, null=True)  # Field name made lowercase.
    device_model = models.CharField(db_column='DEVICE_MODEL', max_length=200, blank=True, null=True)  # Field name made lowercase.
    security_level = models.IntegerField(db_column='SECURITY_LEVEL', blank=True, null=True)  # Field name made lowercase.
    create_date = models.DateTimeField(db_column='CREATE_DATE')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_wechat_pay'


class Users(models.Model):
    username = models.CharField(primary_key=True, max_length=15)
    userpass = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'users'


class VivoScmAccountInfo(models.Model):
    accounts_id = models.IntegerField(blank=True, null=True)
    username = models.CharField(max_length=50, blank=True, null=True)
    ipaddr = models.CharField(max_length=50, blank=True, null=True)
    macaddr = models.CharField(max_length=50, blank=True, null=True)
    info = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vivo_scm_account_info'


class VivoScmAccounts(models.Model):
    username = models.CharField(max_length=50, blank=True, null=True)
    password = models.CharField(max_length=50, blank=True, null=True)
    permissions = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    depart = models.CharField(max_length=50, blank=True, null=True)
    mobile = models.CharField(max_length=25, blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vivo_scm_accounts'


class VivoScmMachines(models.Model):
    machine = models.CharField(max_length=100, blank=True, null=True)
    hostip = models.CharField(max_length=50, blank=True, null=True)
    mac_addr = models.CharField(max_length=50, blank=True, null=True)
    hostname = models.CharField(max_length=50, blank=True, null=True)
    username = models.CharField(max_length=50, blank=True, null=True)
    password = models.CharField(max_length=50, blank=True, null=True)
    cmd = models.CharField(max_length=100, blank=True, null=True)
    login_username = models.CharField(max_length=300, blank=True, null=True)
    control_username = models.CharField(max_length=300, blank=True, null=True)
    type = models.CharField(max_length=4, blank=True, null=True)
    remark1 = models.CharField(max_length=100, blank=True, null=True)
    remark2 = models.CharField(max_length=100, blank=True, null=True)
    remark3 = models.CharField(max_length=100, blank=True, null=True)
    remark4 = models.CharField(max_length=100, blank=True, null=True)
    information = models.CharField(max_length=500, blank=True, null=True)
    brand = models.CharField(max_length=100, blank=True, null=True)
    location = models.CharField(max_length=10, blank=True, null=True)
    asset_tag = models.CharField(max_length=20, blank=True, null=True)
    reg_time = models.CharField(max_length=20, blank=True, null=True)
    flag = models.CharField(max_length=5, blank=True, null=True)
    login_id = models.CharField(max_length=1000, blank=True, null=True)
    control_id = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vivo_scm_machines'


class VivoScmShares(models.Model):
    machine = models.CharField(max_length=50, blank=True, null=True)
    type = models.CharField(max_length=50, blank=True, null=True)
    sharename = models.CharField(max_length=300, blank=True, null=True)
    mountpoint = models.CharField(max_length=100, blank=True, null=True)
    username = models.CharField(max_length=50, blank=True, null=True)
    password = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vivo_scm_shares'
