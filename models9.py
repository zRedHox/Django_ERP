# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AcsMain(models.Model):
    acs_main = models.CharField(primary_key=True, max_length=2)
    acs_desc = models.CharField(max_length=40, blank=True, null=True)
    lastkey = models.DateTimeField()
    lastuser = models.CharField(max_length=30)
    rt_main = models.ForeignKey('GfMainroute', models.DO_NOTHING, db_column='rt_main')

    class Meta:
        managed = False
        db_table = 'acs_main'


class AcsSub(models.Model):
    acs_main = models.CharField(primary_key=True, max_length=2)
    acs_sub = models.CharField(max_length=3)
    acs_desc = models.CharField(max_length=50, blank=True, null=True)
    lastkey = models.DateTimeField()
    lastuser = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'acs_sub'
        unique_together = (('acs_main', 'acs_sub'),)


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
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
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class ComMast(models.Model):
    com_type = models.DecimalField(max_digits=65535, decimal_places=65535)
    com_desc = models.CharField(max_length=50, blank=True, null=True)
    serial_no = models.CharField(max_length=30)
    assets_no = models.CharField(max_length=8, blank=True, null=True)
    supp = models.CharField(max_length=50, blank=True, null=True)
    com_pri = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    size = models.CharField(max_length=5, blank=True, null=True)
    user_dp = models.CharField(max_length=3, blank=True, null=True)
    brand_nme = models.CharField(max_length=20, blank=True, null=True)
    spec = models.CharField(max_length=50, blank=True, null=True)
    ipaddr = models.CharField(max_length=15, blank=True, null=True)
    mainboard = models.CharField(max_length=50, blank=True, null=True)
    cpu = models.CharField(max_length=50, blank=True, null=True)
    ram = models.CharField(max_length=10, blank=True, null=True)
    reg_date = models.DateField(blank=True, null=True)
    key_date = models.DateField(blank=True, null=True)
    key_time = models.CharField(max_length=10, blank=True, null=True)
    key_user = models.CharField(max_length=20, blank=True, null=True)
    id = models.AutoField(unique=True)

    class Meta:
        managed = False
        db_table = 'com_mast'


class ComRepair(models.Model):
    serial_no = models.CharField(max_length=30)
    rp_type = models.CharField(max_length=1, blank=True, null=True)
    rp_date = models.DateField(blank=True, null=True)
    rp_dept = models.CharField(max_length=3, blank=True, null=True)
    rp_desc = models.TextField(blank=True, null=True)
    rev_date = models.DateField(blank=True, null=True)
    rev_pr = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    rp_support = models.CharField(max_length=6, blank=True, null=True)
    key_date = models.DateField(blank=True, null=True)
    key_time = models.CharField(max_length=10, blank=True, null=True)
    key_user = models.CharField(max_length=20, blank=True, null=True)
    rp_repair = models.TextField(blank=True, null=True)
    rp_docno = models.AutoField()
    refr_no = models.CharField(max_length=10, blank=True, null=True)
    chk_comtype = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'com_repair'


class ComType(models.Model):
    com_type = models.CharField(max_length=20, blank=True, null=True)
    id = models.AutoField()

    class Meta:
        managed = False
        db_table = 'com_type'


class CurrType(models.Model):
    curr_type = models.IntegerField(primary_key=True)
    short_name = models.CharField(max_length=10)
    description = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'curr_type'


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
    id = models.BigAutoField(primary_key=True)
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


class EmpStop(models.Model):
    emp_no = models.CharField(max_length=6)
    md_no = models.CharField(max_length=6)
    emp_start = models.DateField(blank=True, null=True)
    emp_end = models.DateField(blank=True, null=True)
    emp_st_tm = models.CharField(max_length=10, blank=True, null=True)
    emp_en_tm = models.CharField(max_length=10, blank=True, null=True)
    emp_type = models.CharField(max_length=2, blank=True, null=True)
    key_date = models.DateField(blank=True, null=True)
    key_time = models.CharField(max_length=10, blank=True, null=True)
    key_user = models.CharField(max_length=20, blank=True, null=True)
    empmd_date = models.DateField()
    emp_dept = models.CharField(max_length=-1)
    empstop_fg = models.CharField(max_length=1, blank=True, null=True)
    empstop_id = models.AutoField()
    empmd_time = models.CharField(max_length=10, blank=True, null=True)
    md_doc_no = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'emp_stop'


class EmpWksub(models.Model):
    emp_no = models.CharField(max_length=6)
    wksub = models.ForeignKey('WkSubstation', models.DO_NOTHING, db_column='wksub_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'emp_wksub'


class Enamel(models.Model):
    pantone = models.CharField(primary_key=True, max_length=10)
    description = models.CharField(max_length=100, blank=True, null=True)
    lastkey = models.DateTimeField()
    lastuser = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'enamel'


class GfDoctype(models.Model):
    doc_type = models.CharField(primary_key=True, max_length=2)
    doc_desc = models.CharField(max_length=80, blank=True, null=True)
    lastkey = models.DateTimeField()
    lastuser = models.CharField(max_length=30, blank=True, null=True)
    last_doc_no = models.CharField(max_length=8)

    class Meta:
        managed = False
        db_table = 'gf_doctype'


class GfEditlog(models.Model):
    log_id = models.BigAutoField(primary_key=True)
    remind_gp = models.CharField(max_length=3)
    edit_time = models.DateTimeField()
    edit_user = models.CharField(max_length=30, blank=True, null=True)
    edit_log = models.TextField(blank=True, null=True)
    edit_note = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gf_editlog'


class GfJobbal(models.Model):
    section_id = models.IntegerField(unique=True)
    job_process = models.ForeignKey('GfJobprocess', models.DO_NOTHING, db_column='job_process')
    job_char = models.CharField(max_length=1)
    pc_qty_in = models.DecimalField(max_digits=10, decimal_places=1, blank=True, null=True)
    wt_in = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    qty_bal = models.DecimalField(max_digits=10, decimal_places=1, blank=True, null=True)
    wt_bal = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    lastkey = models.DateTimeField(blank=True, null=True)
    lastuser = models.CharField(max_length=30, blank=True, null=True)
    rp_qty_in = models.DecimalField(max_digits=10, decimal_places=1, blank=True, null=True)
    qty_work = models.DecimalField(max_digits=10, decimal_places=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gf_jobbal'


class GfJobio(models.Model):
    job_process = models.ForeignKey('GfJobprocess', models.DO_NOTHING, db_column='job_process')
    job_char = models.CharField(max_length=1)
    doc_date = models.DateTimeField()
    from_section = models.ForeignKey('GfSection', models.DO_NOTHING)
    to_section = models.ForeignKey('GfSection', models.DO_NOTHING)
    doc_type = models.ForeignKey(GfDoctype, models.DO_NOTHING, db_column='doc_type')
    doc_qty = models.DecimalField(max_digits=10, decimal_places=1)
    doc_wt = models.DecimalField(max_digits=10, decimal_places=2)
    doc_loss_wt = models.DecimalField(max_digits=10, decimal_places=2)
    to_accept = models.CharField(max_length=1, blank=True, null=True)
    accept_date = models.DateTimeField(blank=True, null=True)
    accept_user = models.CharField(max_length=30, blank=True, null=True)
    to_return = models.CharField(max_length=1, blank=True, null=True)
    return_date = models.DateTimeField(blank=True, null=True)
    return_user = models.CharField(max_length=30, blank=True, null=True)
    from_accept_rt = models.CharField(max_length=1, blank=True, null=True)
    accept_rt_date = models.DateTimeField(blank=True, null=True)
    accept_rt_user = models.CharField(max_length=30, blank=True, null=True)
    doc_user = models.CharField(max_length=30)
    doc_prn_no = models.CharField(max_length=7, blank=True, null=True)
    log = models.ForeignKey(GfEditlog, models.DO_NOTHING, blank=True, null=True)
    doc_id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'gf_jobio'


class GfJobprocess(models.Model):
    job_process = models.CharField(primary_key=True, max_length=8)
    pack_qty = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    bal_qty = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    lastkey = models.DateTimeField()
    lastuser = models.CharField(max_length=-1)
    date_req = models.DateField()
    job_group_fg = models.CharField(max_length=1)
    plant_code = models.CharField(max_length=2)

    class Meta:
        managed = False
        db_table = 'gf_jobprocess'


class GfJobsemi(models.Model):
    job_char = models.CharField(max_length=1)
    lastkey = models.DateTimeField()
    lastuser = models.CharField(max_length=30)
    semi_route = models.ForeignKey('SemiRouteId', models.DO_NOTHING)
    job_process = models.OneToOneField(GfJobprocess, models.DO_NOTHING, db_column='job_process', primary_key=True)

    class Meta:
        managed = False
        db_table = 'gf_jobsemi'
        unique_together = (('job_process', 'job_char'),)


class GfLogin(models.Model):
    gf_user = models.CharField(primary_key=True, max_length=6)
    gf_pass = models.CharField(max_length=10)
    master = models.CharField(max_length=2, blank=True, null=True)
    it = models.CharField(max_length=2, blank=True, null=True)
    model = models.CharField(max_length=2, blank=True, null=True)
    store = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gf_login'


class GfLoginsystem(models.Model):
    gf_user = models.ForeignKey(GfLogin, models.DO_NOTHING, db_column='gf_user')
    system = models.ForeignKey('GfSystem', models.DO_NOTHING)
    lastuser = models.CharField(max_length=30)
    lastkey = models.DateTimeField()
    level = models.IntegerField()
    main = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gf_loginsystem'
        unique_together = (('gf_user', 'system'),)


class GfMainroute(models.Model):
    rt_main = models.CharField(primary_key=True, max_length=2)
    rt_desc = models.CharField(max_length=40)
    rt_section_fg = models.CharField(max_length=1)
    rt_max_insection = models.IntegerField()
    lastkey = models.DateTimeField()
    lastuser = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'gf_mainroute'


class GfMoldtype(models.Model):
    mold_type = models.CharField(primary_key=True, max_length=2)
    mold_desc = models.CharField(max_length=80)
    lastkey = models.DateTimeField()
    lastuser = models.CharField(max_length=30)
    model_fg = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gf_moldtype'


class GfPlant(models.Model):
    plant_code = models.CharField(primary_key=True, max_length=2)
    plant_desc = models.CharField(max_length=15)
    lastkey = models.DateTimeField()
    lastuser = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'gf_plant'


class GfRoutecode(models.Model):
    rt_code = models.CharField(max_length=8)
    routecode_id = models.AutoField(primary_key=True)
    rt_desc = models.CharField(max_length=100, blank=True, null=True)
    s_std = models.IntegerField(blank=True, null=True)
    g_std = models.IntegerField(blank=True, null=True)
    rt_unit = models.CharField(max_length=50, blank=True, null=True)
    lastkey = models.DateTimeField()
    lastuser = models.CharField(max_length=30)
    rt_spec = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gf_routecode'


class GfSection(models.Model):
    section_id = models.AutoField(primary_key=True)
    plant_code = models.ForeignKey(GfPlant, models.DO_NOTHING, db_column='plant_code')
    rt_main = models.ForeignKey(GfMainroute, models.DO_NOTHING, db_column='rt_main')
    rt_loop = models.IntegerField(blank=True, null=True)
    lastkey = models.DateTimeField()
    lastuser = models.CharField(max_length=30)
    bp_deptab = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gf_section'


class GfSemi(models.Model):
    semi_code = models.CharField(primary_key=True, max_length=30)
    semi_desc = models.CharField(max_length=200, blank=True, null=True)
    lastkey = models.DateTimeField()
    lastuser = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'gf_semi'


class GfStockcode(models.Model):
    stockgroup = models.ForeignKey('GfStockgroup', models.DO_NOTHING, db_column='stockgroup')
    stockcode = models.CharField(max_length=19)
    stockdesc = models.CharField(max_length=300, blank=True, null=True)
    unit_qty = models.CharField(max_length=100, blank=True, null=True)
    unit_volume = models.CharField(max_length=100, blank=True, null=True)
    std_wt_gm = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    std_pr_bt = models.DecimalField(max_digits=11, decimal_places=4, blank=True, null=True)
    std_pr_us = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    std_sale_bt = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    std_sale_us = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    std_lb_bt = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    std_lb_us = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    lastkey = models.DateTimeField()
    lastuser = models.CharField(max_length=30)
    std_unit = models.CharField(max_length=1, blank=True, null=True)
    mt_metal = models.ForeignKey('MtMetal', models.DO_NOTHING, db_column='mt_metal', blank=True, null=True)
    eng_desc = models.CharField(max_length=500, blank=True, null=True)
    eng_unit_qty = models.CharField(max_length=50, blank=True, null=True)
    eng_unit_volume = models.CharField(max_length=50, blank=True, null=True)
    max_stock = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    min_stock = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    reorder = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    order_time = models.IntegerField(blank=True, null=True)
    old_code = models.CharField(max_length=19, blank=True, null=True)
    maxmin_fg = models.CharField(max_length=1, blank=True, null=True)
    stock_status = models.CharField(max_length=1, blank=True, null=True)
    keep_stock = models.CharField(max_length=1, blank=True, null=True)
    remark = models.TextField(blank=True, null=True)
    purchase_fg = models.CharField(max_length=1, blank=True, null=True)
    mt_group = models.ForeignKey('MtGroup', models.DO_NOTHING, db_column='mt_group', blank=True, null=True)
    cus = models.ForeignKey('Wfcust', models.DO_NOTHING, blank=True, null=True)
    account_type = models.CharField(max_length=1, blank=True, null=True)
    std_lb_time = models.IntegerField(blank=True, null=True)
    lb_remark = models.TextField(blank=True, null=True)
    surface = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    location = models.CharField(max_length=150, blank=True, null=True)
    sp_s_unit = models.CharField(max_length=30, blank=True, null=True)
    sp_u_conv = models.DecimalField(max_digits=6, decimal_places=0, blank=True, null=True)
    have_lb = models.CharField(max_length=1, blank=True, null=True)
    stock_id = models.AutoField(primary_key=True)
    sp_check = models.CharField(max_length=1, blank=True, null=True)

    # A unique constraint could not be introspected.
    class Meta:
        managed = False
        db_table = 'gf_stockcode'
        unique_together = (('stockgroup', 'stockcode'),)


class GfStockgroup(models.Model):
    stockgroup = models.CharField(primary_key=True, max_length=2)
    desc = models.TextField(blank=True, null=True)
    lastkey = models.DateTimeField()
    lastuser = models.CharField(max_length=30)
    header_table = models.TextField(blank=True, null=True)
    metal_fg = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'gf_stockgroup'


class GfStockio(models.Model):
    stock = models.ForeignKey(GfStockcode, models.DO_NOTHING)
    doc_type = models.ForeignKey(GfDoctype, models.DO_NOTHING, db_column='doc_type')
    stock_type = models.CharField(max_length=1, blank=True, null=True)
    doc_qty = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    doc_wt = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    doc_unit = models.CharField(max_length=30, blank=True, null=True)
    stock_qty = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    stock_wt = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    stock_u_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    stock_amt = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    stock_qty_bal = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    stock_wt_bal = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    stock_amt_bal = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    doc_date = models.DateField(blank=True, null=True)
    stock_date = models.DateTimeField()
    lastdate = models.DateTimeField()
    lastuser = models.CharField(max_length=30)
    stockio_id = models.AutoField(primary_key=True)
    job_process = models.ForeignKey(GfJobprocess, models.DO_NOTHING, db_column='job_process', blank=True, null=True)
    job_char = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'gf_stockio'


class GfStockuse(models.Model):
    job_process = models.OneToOneField(GfJobprocess, models.DO_NOTHING, db_column='job_process', primary_key=True)
    job_char = models.CharField(max_length=1)
    stock = models.ForeignKey(GfStockcode, models.DO_NOTHING)
    unit_use = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total_use = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    prepare = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    issue = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    lastkey = models.DateTimeField()
    lastuser = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'gf_stockuse'
        unique_together = (('job_process', 'job_char', 'stock'),)


class GfSubroute(models.Model):
    rt_main = models.ForeignKey(GfMainroute, models.DO_NOTHING, db_column='rt_main')
    rt_sub = models.CharField(max_length=3)
    rt_desc = models.CharField(max_length=80, blank=True, null=True)
    lastkey = models.DateTimeField()
    lastuser = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'gf_subroute'
        unique_together = (('rt_main', 'rt_sub'),)


class GfSystem(models.Model):
    system_id = models.AutoField(primary_key=True)
    system_name = models.CharField(max_length=20, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    lastkey = models.DateTimeField()
    keyuser = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'gf_system'


class Gfmaster(models.Model):
    pro_code = models.CharField(primary_key=True, max_length=9)
    pro_type = models.ForeignKey('ProType', models.DO_NOTHING, db_column='pro_type')
    std_925_wt = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    mold_wt = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    mold_metal = models.CharField(max_length=3, blank=True, null=True)
    search_tag1 = models.TextField(blank=True, null=True)
    search_tag2 = models.TextField(blank=True, null=True)
    search_tag3 = models.TextField(blank=True, null=True)
    remark = models.TextField(blank=True, null=True)
    lastuser = models.CharField(max_length=30)
    surface = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    lastkey = models.DateTimeField()
    hallmark = models.IntegerField(blank=True, null=True)
    cus = models.ForeignKey('Wfcust', models.DO_NOTHING, blank=True, null=True)
    route_check = models.CharField(max_length=1, blank=True, null=True)
    route_checkdate = models.DateTimeField(blank=True, null=True)
    route_checkuser = models.CharField(max_length=30, blank=True, null=True)
    pd_gd = models.CharField(max_length=2, blank=True, null=True)
    route_remark = models.TextField(blank=True, null=True)
    sale_remark = models.TextField(blank=True, null=True)
    mold_type = models.CharField(max_length=2, blank=True, null=True)
    mold_model = models.CharField(max_length=9, blank=True, null=True)
    cast_925wt = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    yg_wt = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    yg_castwt = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    cus_yg_wt = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    wg_wt = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    wg_castwt = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    cus_wg_wt = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    pt_wt = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    cus_pt_wt = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    si_wt = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    cus_si_wt = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    br_wt = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    cus_br_wt = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    ag_wt = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    sil_chain = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    true_wt = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    no_cast = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gfmaster'


class Gfpict(models.Model):
    pro_code = models.CharField(primary_key=True, max_length=9)
    img_data_text = models.TextField(blank=True, null=True)
    img_data_bytea = models.BinaryField(blank=True, null=True)
    lastkey = models.DateTimeField()
    lastuser = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gfpict'


class Gfsol(models.Model):
    pro_code = models.CharField(primary_key=True, max_length=9)
    img_data_bytea = models.BinaryField(blank=True, null=True)
    lastkey = models.DateTimeField()
    lastuser = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'gfsol'


class Ji300(models.Model):
    jino = models.CharField(max_length=7, blank=True, null=True)
    jistcd = models.CharField(max_length=5, blank=True, null=True)
    jiwt = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ji300'


class LockSc001(models.Model):
    md_sc_cd = models.CharField(max_length=3)
    md_metal = models.CharField(max_length=3)
    from_ui = models.CharField(max_length=20)
    from_user = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'lock_sc001'
        unique_together = (('md_sc_cd', 'md_metal'),)


class MdMaster(models.Model):
    md_no = models.CharField(unique=True, max_length=6)
    md_model = models.CharField(max_length=9)
    md_date = models.DateField(blank=True, null=True)
    md_fndate = models.DateField(blank=True, null=True)
    md_dl = models.DateField(blank=True, null=True)
    cus_no = models.CharField(max_length=10, blank=True, null=True)
    md_type = models.CharField(max_length=1, blank=True, null=True)
    md_time = models.CharField(max_length=10, blank=True, null=True)
    md_end_d = models.DateField(blank=True, null=True)
    md_end_type = models.CharField(max_length=1, blank=True, null=True)
    md_end = models.CharField(max_length=1, blank=True, null=True)
    md_qty = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    md_branch = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    md_met = models.CharField(max_length=3, blank=True, null=True)
    md_sc_cd = models.CharField(max_length=3, blank=True, null=True)
    key_date = models.DateField()
    key_time = models.CharField(max_length=10)
    key_user = models.CharField(max_length=20)
    od_no = models.CharField(max_length=6, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'md_master'


class MsInout(models.Model):
    md_no = models.ForeignKey(MdMaster, models.DO_NOTHING, db_column='md_no')
    md_sc_cd = models.CharField(max_length=3, blank=True, null=True)
    md_date = models.DateField(blank=True, null=True)
    md_end_d = models.DateField(blank=True, null=True)
    md_qty = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    md_type = models.ForeignKey('ScMastd', models.DO_NOTHING, db_column='md_type', blank=True, null=True)
    md_wk = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    md_wt = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    md_rtwt = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    key_date = models.DateField()
    key_time = models.CharField(max_length=10)
    key_user = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'ms_inout'
        unique_together = (('md_no', 'md_sc_cd'),)


class MsInoutd(models.Model):
    md_no = models.ForeignKey(MdMaster, models.DO_NOTHING, db_column='md_no')
    md_sc_cd = models.CharField(max_length=3)
    md_status = models.ForeignKey('ScMastd', models.DO_NOTHING, db_column='md_status')
    md_date = models.DateField(blank=True, null=True)
    md_end = models.DateField(blank=True, null=True)
    key_date = models.DateField()
    key_time = models.CharField(max_length=10)
    key_user = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'ms_inoutd'


class MsInouttf(models.Model):
    md_no = models.ForeignKey(MdMaster, models.DO_NOTHING, db_column='md_no')
    md_doc_no = models.AutoField(unique=True)
    md_sc_from = models.CharField(max_length=3)
    md_sc_to = models.CharField(max_length=3)
    md_date = models.DateField()
    md_qty = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    md_time = models.CharField(max_length=8)
    md_wt = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    key_user = models.CharField(max_length=20)
    md_chkin = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ms_inouttf'


class MsIoEmp(models.Model):
    md_no = models.ForeignKey(MsInout, models.DO_NOTHING, db_column='md_no')
    md_sc_cd = models.CharField(max_length=3)
    md_emp = models.CharField(max_length=6)
    md_date = models.DateField()
    md_end = models.DateField(blank=True, null=True)
    md_qty = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    md_wk = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    md_point = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    md_wt = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    md_rtwt = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    key_date = models.DateField()
    key_time = models.CharField(max_length=10)
    key_user = models.CharField(max_length=20)
    md_per = models.IntegerField(blank=True, null=True)
    transf_id = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ms_io_emp'


class MsIoprototype(models.Model):
    ms_emp_no = models.CharField(max_length=6)
    ms_wksub_from = models.IntegerField()
    ms_wksub_to = models.ForeignKey('WkSubstation', models.DO_NOTHING, db_column='ms_wksub_to')
    ms_in_date = models.DateField(blank=True, null=True)
    ms_in_time = models.CharField(max_length=10, blank=True, null=True)
    key_user = models.CharField(max_length=20, blank=True, null=True)
    ms_job_no = models.CharField(max_length=8)

    class Meta:
        managed = False
        db_table = 'ms_ioprototype'


class MsIssue(models.Model):
    ms_no = models.AutoField()
    ms_model = models.CharField(max_length=9, blank=True, null=True)
    ms_emp = models.CharField(max_length=6, blank=True, null=True)
    ms_qty = models.IntegerField(blank=True, null=True)
    ms_dept = models.CharField(max_length=10, blank=True, null=True)
    ms_date = models.DateField(blank=True, null=True)
    ms_rtdate = models.DateField(blank=True, null=True)
    ms_remark = models.CharField(max_length=200, blank=True, null=True)
    key_date = models.DateField(blank=True, null=True)
    key_time = models.CharField(max_length=10, blank=True, null=True)
    key_user = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ms_issue'


class MsJi300(models.Model):
    md_no = models.ForeignKey(MdMaster, models.DO_NOTHING, db_column='md_no')
    md_wt = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    id = models.ForeignKey(Ji300, models.DO_NOTHING, db_column='id', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ms_ji300'


class MsPrototype(models.Model):
    ms_job_no = models.CharField(max_length=8, blank=True, null=True)
    ms_wksub = models.ForeignKey('WkSubstation', models.DO_NOTHING, db_column='ms_wksub_ID', blank=True, null=True)  # Field name made lowercase.
    ms_in_date = models.DateField(blank=True, null=True)
    ms_in_time = models.CharField(max_length=10, blank=True, null=True)
    key_user = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ms_prototype'


class MsRepair(models.Model):
    ms_model = models.CharField(primary_key=True, max_length=9)
    rp_qty = models.IntegerField(blank=True, null=True)
    rp_locate = models.CharField(max_length=50, blank=True, null=True)
    rp_remark = models.CharField(max_length=100, blank=True, null=True)
    rp_sort = models.CharField(max_length=10, blank=True, null=True)
    rp_prn = models.CharField(max_length=1, blank=True, null=True)
    key_date = models.DateField()
    key_time = models.CharField(max_length=10)
    key_user = models.CharField(max_length=20)
    sys_date = models.DateField(blank=True, null=True)
    sys_time = models.CharField(max_length=10, blank=True, null=True)
    sys_user = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ms_repair'


class MsStkcard(models.Model):
    md_model = models.OneToOneField('MsStockfg', models.DO_NOTHING, db_column='md_model', primary_key=True)
    doc_no = models.CharField(max_length=10)
    doc_date = models.DateField()
    doc_type = models.CharField(max_length=1)
    md_qty = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    md_wt = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    md_remark = models.CharField(max_length=80, blank=True, null=True)
    md_locate = models.CharField(max_length=50, blank=True, null=True)
    key_date = models.DateField()
    key_time = models.CharField(max_length=10)
    key_user = models.CharField(max_length=20)
    md_met = models.CharField(max_length=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ms_stkcard'
        unique_together = (('md_model', 'doc_date', 'doc_no', 'doc_type'),)


class MsStkemp(models.Model):
    md_sc_cd = models.CharField(max_length=3)
    md_emp = models.CharField(max_length=6)
    md_date = models.DateField(blank=True, null=True)
    md_wt = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    md_model = models.CharField(max_length=9, blank=True, null=True)
    md_bal = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    st_type = models.CharField(max_length=2)
    key_date = models.DateField()
    key_time = models.CharField(max_length=10)
    key_user = models.CharField(max_length=20)
    md_no = models.CharField(max_length=6)
    md_metal = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'ms_stkemp'


class MsStkmetal(models.Model):
    md_sc_cd = models.CharField(max_length=3)
    md_metal = models.CharField(max_length=3)
    md_date = models.DateField(blank=True, null=True)
    md_wt = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    md_bal = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    st_type = models.CharField(max_length=1)
    key_date = models.DateField()
    key_time = models.CharField(max_length=10)
    key_user = models.CharField(max_length=20)
    md_doc_no = models.IntegerField()
    md_doc_type = models.CharField(max_length=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ms_stkmetal'


class MsStockfg(models.Model):
    md_model = models.CharField(primary_key=True, max_length=9)
    md_met = models.CharField(max_length=3)
    md_join_q = models.IntegerField(blank=True, null=True)
    md_adj_q = models.IntegerField(blank=True, null=True)
    md_total_q = models.IntegerField(blank=True, null=True)
    md_join_wt = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    md_adj_wt = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    md_total_wt = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    md_remark = models.CharField(max_length=80, blank=True, null=True)
    md_chk = models.CharField(max_length=1, blank=True, null=True)
    md_locate = models.CharField(max_length=50, blank=True, null=True)
    key_date = models.DateField()
    key_time = models.CharField(max_length=10)
    key_user = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'ms_stockfg'
        unique_together = (('md_model', 'md_met'),)


class Msioempback(models.Model):
    md_no = models.CharField(max_length=6, blank=True, null=True)
    md_sc_cd = models.CharField(max_length=3, blank=True, null=True)
    md_emp = models.CharField(max_length=6, blank=True, null=True)
    md_date = models.DateField()
    md_end = models.DateField(blank=True, null=True)
    md_qty = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    md_wk = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    md_point = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    md_wt = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    md_rtwt = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    key_date = models.DateField()
    key_time = models.CharField(max_length=10, blank=True, null=True)
    key_user = models.CharField(max_length=20, blank=True, null=True)
    md_per = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    transf_id = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'msioempback'


class MtColor(models.Model):
    mt_color = models.CharField(primary_key=True, max_length=1)
    mt_desc = models.CharField(max_length=20, blank=True, null=True)
    lastkey = models.DateTimeField()
    lastuser = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'mt_color'


class MtGroup(models.Model):
    mt_group = models.CharField(primary_key=True, max_length=2)
    mt_desc = models.CharField(max_length=200, blank=True, null=True)
    lastkey = models.DateTimeField()
    lastuser = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'mt_group'


class MtMetal(models.Model):
    mt_metal = models.CharField(primary_key=True, max_length=3)
    mt_desc = models.CharField(max_length=90, blank=True, null=True)
    mt_cal = models.CharField(max_length=3, blank=True, null=True)
    mt_multi = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    mt_add = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    mt_pure = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    mt_alloy = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    alloy_date = models.DateTimeField(blank=True, null=True)
    old_alloy = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    mt_show = models.CharField(max_length=3, blank=True, null=True)
    lastkey = models.DateTimeField()
    lastuser = models.CharField(max_length=30)
    mt_color = models.ForeignKey(MtColor, models.DO_NOTHING, db_column='mt_color', blank=True, null=True)
    mt_925tf = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mt_metal'


class MtMetald(models.Model):
    mt_metal = models.ForeignKey(MtMetal, models.DO_NOTHING, db_column='mt_metal')
    sub_metal = models.ForeignKey(MtMetal, models.DO_NOTHING, db_column='sub_metal')
    lastkey = models.DateTimeField()
    lastuser = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'mt_metald'
        unique_together = (('mt_metal', 'sub_metal'),)


class PlatChem(models.Model):
    chem_no = models.CharField(primary_key=True, max_length=3)
    description = models.CharField(max_length=150, blank=True, null=True)
    factor = models.DecimalField(max_digits=8, decimal_places=2)
    density = models.DecimalField(max_digits=8, decimal_places=2)
    chem = models.CharField(max_length=1, blank=True, null=True)
    surface = models.CharField(max_length=1, blank=True, null=True)
    light = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    plat_pri = models.CharField(max_length=2, blank=True, null=True)
    ch_pri = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    speed = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    coat_fg = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    pure_mt = models.CharField(max_length=5, blank=True, null=True)
    remark = models.TextField(blank=True, null=True)
    lastkey = models.DateTimeField()
    lastuser = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'plat_chem'


class PlatSeq(models.Model):
    plat_type = models.ForeignKey('PlatType', models.DO_NOTHING, db_column='plat_type')
    seq = models.CharField(max_length=2)
    chem_no = models.ForeignKey(PlatChem, models.DO_NOTHING, db_column='chem_no')
    micron = models.DecimalField(max_digits=8, decimal_places=2)
    rho = models.CharField(max_length=1, blank=True, null=True)
    lastkey = models.DateTimeField()
    lastuser = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'plat_seq'


class PlatType(models.Model):
    plat_type = models.CharField(primary_key=True, max_length=5)
    description = models.CharField(max_length=200, blank=True, null=True)
    micron = models.DecimalField(max_digits=8, decimal_places=2)
    mt_metal = models.ForeignKey(MtMetal, models.DO_NOTHING, db_column='mt_metal', blank=True, null=True)
    plating = models.ForeignKey('Plating', models.DO_NOTHING, db_column='plating')
    surf = models.CharField(max_length=1)
    lastkey = models.DateTimeField()
    lastuser = models.CharField(max_length=30)
    remark = models.TextField(blank=True, null=True)
    remarkpr = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'plat_type'


class Plating(models.Model):
    plating = models.CharField(primary_key=True, max_length=2)
    description = models.CharField(max_length=200, blank=True, null=True)
    surf = models.CharField(max_length=1)
    lastkey = models.DateTimeField()
    lastuser = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'plating'


class ProBom(models.Model):
    pro_sub = models.ForeignKey('ProSub', models.DO_NOTHING)
    stock_id = models.BigIntegerField()
    qty = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    route_seq_id = models.BigIntegerField(blank=True, null=True)
    lastkey = models.DateTimeField()
    lastuser = models.CharField(max_length=30)
    bomdata_id = models.AutoField(primary_key=True)
    seq = models.CharField(max_length=3, blank=True, null=True)
    setting = models.ForeignKey('Setting', models.DO_NOTHING, db_column='setting', blank=True, null=True)
    wax_fg = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pro_bom'


class ProCoat(models.Model):
    pro_code = models.ForeignKey(Gfmaster, models.DO_NOTHING, db_column='pro_code')
    plat_type = models.ForeignKey(PlatType, models.DO_NOTHING, db_column='plat_type')
    lastkey = models.DateTimeField()
    lastuser = models.CharField(max_length=30)
    remark = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pro_coat'
        unique_together = (('pro_code', 'plat_type'),)


class ProEna(models.Model):
    pro_sub = models.ForeignKey('ProSub', models.DO_NOTHING)
    pantone = models.ForeignKey(Enamel, models.DO_NOTHING, db_column='pantone')
    pn_no = models.CharField(max_length=3)
    lastkey = models.DateTimeField()
    lastuser = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'pro_ena'
        unique_together = (('pro_sub', 'pantone', 'pn_no'),)


class ProMetal(models.Model):
    pro_code = models.OneToOneField('ProMetalbase', models.DO_NOTHING, db_column='pro_code', primary_key=True)
    mt_metal = models.CharField(max_length=3)
    sub_metal = models.CharField(max_length=3)
    true_wt = models.DecimalField(max_digits=9, decimal_places=3, blank=True, null=True)
    std_conv_wt = models.DecimalField(max_digits=8, decimal_places=2)
    wax_wt = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    fin_wt = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    lastkey = models.DateTimeField()
    lastuser = models.CharField(max_length=30)
    cus_wt = models.DecimalField(max_digits=9, decimal_places=3, blank=True, null=True)
    cast_wt = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    mt_cast = models.CharField(max_length=1, blank=True, null=True)
    mt_mast = models.CharField(max_length=1, blank=True, null=True)
    stn_set = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pro_metal'
        unique_together = (('pro_code', 'mt_metal', 'sub_metal'),)


class ProMetalbase(models.Model):
    pro_code = models.ForeignKey(Gfmaster, models.DO_NOTHING, db_column='pro_code')
    mt_metal = models.ForeignKey(MtMetal, models.DO_NOTHING, db_column='mt_metal')
    lastkey = models.DateTimeField()
    lastuser = models.CharField(max_length=30)
    pro_metal_id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'pro_metalbase'
        unique_together = (('pro_code', 'mt_metal'),)


class ProMetalbom(models.Model):
    pro_metal = models.ForeignKey(ProMetalbase, models.DO_NOTHING)
    stock = models.ForeignKey(GfStockcode, models.DO_NOTHING)
    qty = models.DecimalField(max_digits=10, decimal_places=2)
    route_seq_id = models.IntegerField(blank=True, null=True)
    lastkey = models.DateTimeField()
    lastuser = models.CharField(max_length=30)
    bomdata_id = models.AutoField(primary_key=True)
    semi_char = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pro_metalbom'


class ProRingsize(models.Model):
    ring_size = models.CharField(max_length=5)
    lastkey = models.DateTimeField()
    lastuser = models.CharField(max_length=30)
    pro_code = models.ForeignKey(Gfmaster, models.DO_NOTHING, db_column='pro_code')

    class Meta:
        managed = False
        db_table = 'pro_ringsize'
        unique_together = (('pro_code', 'ring_size'),)


class ProRoutegroup(models.Model):
    pro_code = models.CharField(max_length=9)
    routegroup = models.CharField(max_length=2)
    base_sub = models.ForeignKey('ProSub', models.DO_NOTHING, blank=True, null=True)
    lastkey = models.DateTimeField()
    lastuser = models.CharField(max_length=30)
    description = models.CharField(max_length=80, blank=True, null=True)
    complete = models.CharField(max_length=1, blank=True, null=True)
    complete_date = models.DateTimeField(blank=True, null=True)
    complete_user = models.CharField(max_length=30, blank=True, null=True)
    route_type = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pro_routegroup'
        unique_together = (('pro_code', 'routegroup'),)


class ProSemi(models.Model):
    semi_code = models.ForeignKey(GfSemi, models.DO_NOTHING, db_column='semi_code', blank=True, null=True)
    semi_char = models.CharField(max_length=1)
    lastkey = models.DateTimeField()
    lastuser = models.CharField(max_length=30)
    cast_metal = models.CharField(max_length=3, blank=True, null=True)
    pro_code = models.ForeignKey(ProRoutegroup, models.DO_NOTHING, db_column='pro_code')
    routegroup = models.CharField(max_length=2)

    class Meta:
        managed = False
        db_table = 'pro_semi'


class ProSpec(models.Model):
    pro_code = models.OneToOneField(Gfmaster, models.DO_NOTHING, db_column='pro_code', primary_key=True)
    pd_spec = models.TextField(blank=True, null=True)
    lastkey = models.DateTimeField()
    lastuser = models.CharField(max_length=30)
    rt_main = models.ForeignKey(GfMainroute, models.DO_NOTHING, db_column='rt_main')

    class Meta:
        managed = False
        db_table = 'pro_spec'
        unique_together = (('pro_code', 'rt_main'),)


class ProSub(models.Model):
    pro_code = models.ForeignKey(Gfmaster, models.DO_NOTHING, db_column='pro_code')
    pro_sub = models.CharField(max_length=2)
    mt_metal = models.CharField(max_length=3)
    description = models.CharField(max_length=80, blank=True, null=True)
    lastkey = models.DateTimeField()
    lastuser = models.CharField(max_length=30)
    pro_sub_id = models.AutoField(primary_key=True)
    metal_check = models.CharField(max_length=1, blank=True, null=True)
    metal_checkdate = models.DateTimeField(blank=True, null=True)
    metal_checkuser = models.CharField(max_length=30, blank=True, null=True)
    routegroup = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pro_sub'
        unique_together = (('pro_code', 'pro_sub'),)


class ProSubmetchar(models.Model):
    pro_code = models.ForeignKey(ProRoutegroup, models.DO_NOTHING, db_column='pro_code')
    routegroup = models.CharField(max_length=2)
    mt_metal = models.CharField(max_length=3)
    sub_metal = models.CharField(max_length=3)
    semi_char = models.CharField(max_length=1)
    lastkey = models.DateTimeField()
    lastuser = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'pro_submetchar'


class ProType(models.Model):
    pro_type = models.CharField(primary_key=True, max_length=2)
    desc_en = models.CharField(max_length=30, blank=True, null=True)
    unit_en = models.CharField(max_length=3)
    desc_th = models.CharField(max_length=50, blank=True, null=True)
    unit_th = models.CharField(max_length=30)
    lastkey = models.DateTimeField()
    lastuser = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'pro_type'


class Remind(models.Model):
    system = models.ForeignKey(GfSystem, models.DO_NOTHING)
    log = models.ForeignKey(GfEditlog, models.DO_NOTHING)
    checkdate = models.DateTimeField(blank=True, null=True)
    checkuser = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'remind'


class RemindGp(models.Model):
    remind_gp = models.CharField(primary_key=True, max_length=3)
    description = models.CharField(max_length=30, blank=True, null=True)
    lastkey = models.DateTimeField()
    lastuser = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'remind_gp'


class RemindSystem(models.Model):
    remind_gp = models.ForeignKey(RemindGp, models.DO_NOTHING, db_column='remind_gp')
    lastkey = models.DateTimeField()
    lastuser = models.CharField(max_length=30)
    system = models.OneToOneField(GfSystem, models.DO_NOTHING, primary_key=True)

    class Meta:
        managed = False
        db_table = 'remind_system'
        unique_together = (('system', 'remind_gp'),)


class Sc001(models.Model):
    sc_code = models.CharField(unique=True, max_length=3)
    sc_name = models.CharField(max_length=50, blank=True, null=True)
    sc_empcode = models.CharField(max_length=2, blank=True, null=True)
    sc_old = models.CharField(max_length=2, blank=True, null=True)
    sc_short = models.CharField(max_length=20, blank=True, null=True)
    sc_mfile = models.CharField(max_length=2, blank=True, null=True)
    key_date = models.DateField(blank=True, null=True)
    key_time = models.CharField(max_length=-1, blank=True, null=True)
    key_user = models.CharField(max_length=20, blank=True, null=True)
    sc_use = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sc_001'


class Sc004(models.Model):
    sc_code = models.CharField(max_length=3)
    sc_name = models.CharField(max_length=15, blank=True, null=True)
    sc_dp_code = models.CharField(max_length=8, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sc_004'


class ScMastd(models.Model):
    sc_code = models.CharField(primary_key=True, max_length=2)
    sc_name = models.CharField(max_length=50, blank=True, null=True)
    key_date = models.DateField(blank=True, null=True)
    key_time = models.CharField(max_length=10, blank=True, null=True)
    key_user = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sc_mastd'


class ScTransfer(models.Model):
    transf_id = models.CharField(max_length=1)
    transf_desc = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sc_transfer'


class SemiRoute(models.Model):
    route_seq_id = models.AutoField(primary_key=True)
    semi_route = models.ForeignKey('SemiRouteId', models.DO_NOTHING)
    routecode = models.ForeignKey(GfRoutecode, models.DO_NOTHING, blank=True, null=True)
    rt_loop = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    work_desc = models.TextField(blank=True, null=True)
    route_seq = models.CharField(max_length=6, blank=True, null=True)
    qty = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    u_stdtime_sec = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    p_realtime_sec = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    lastkey = models.DateTimeField()
    lastuser = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'semi_route'
        unique_together = (('semi_route', 'route_seq'),)


class SemiRouteId(models.Model):
    semi_code = models.ForeignKey(GfSemi, models.DO_NOTHING, db_column='semi_code')
    active = models.CharField(max_length=1)
    lastkey = models.DateTimeField()
    lastuser = models.CharField(max_length=30)
    complete = models.CharField(max_length=1, blank=True, null=True)
    complete_date = models.DateTimeField(blank=True, null=True)
    complete_user = models.CharField(max_length=30, blank=True, null=True)
    semi_route_id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'semi_route_id'


class Setting(models.Model):
    setting = models.CharField(primary_key=True, max_length=2)
    description = models.CharField(max_length=80, blank=True, null=True)
    settype = models.CharField(max_length=2, blank=True, null=True)
    sh_desc = models.CharField(max_length=10, blank=True, null=True)
    lastkey = models.DateTimeField()
    lastuser = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'setting'


class SpMain(models.Model):
    sp_main = models.CharField(primary_key=True, max_length=2)
    sp_desc = models.CharField(max_length=80, blank=True, null=True)
    sp_job = models.CharField(max_length=1)
    lastkey = models.DateTimeField()
    lastuser = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'sp_main'


class SpSub(models.Model):
    sp_sub = models.CharField(primary_key=True, max_length=3)
    sp_desc = models.CharField(max_length=80, blank=True, null=True)
    sp_main = models.ForeignKey(SpMain, models.DO_NOTHING, db_column='sp_main')
    job_fg = models.CharField(max_length=1, blank=True, null=True)
    lastkey = models.DateTimeField()
    lastuser = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'sp_sub'
        unique_together = (('sp_sub', 'sp_main'),)


class StBott(models.Model):
    st_bott = models.CharField(primary_key=True, max_length=2)
    st_desc = models.CharField(max_length=100, blank=True, null=True)
    lastkey = models.DateTimeField()
    lastuser = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'st_bott'


class StFancy(models.Model):
    st_new = models.CharField(primary_key=True, max_length=15)
    st_newold = models.CharField(max_length=15, blank=True, null=True)
    st_old = models.CharField(max_length=5, blank=True, null=True)
    st_shape = models.ForeignKey('StShape', models.DO_NOTHING, db_column='st_shape', blank=True, null=True)
    st_width = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    st_long = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    st_front = models.ForeignKey('StFront', models.DO_NOTHING, db_column='st_front', blank=True, null=True)
    st_bott = models.ForeignKey(StBott, models.DO_NOTHING, db_column='st_bott', blank=True, null=True)
    st_h_font = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    st_h_bott = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    st_h_line = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    st_h_cross = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    st_remark = models.TextField(blank=True, null=True)
    lastkey = models.DateTimeField()
    lastuser = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'st_fancy'


class StFront(models.Model):
    st_front = models.CharField(primary_key=True, max_length=2)
    st_desc = models.CharField(max_length=100, blank=True, null=True)
    lastkey = models.DateTimeField()
    lastuser = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'st_front'


class StGrade(models.Model):
    st_grade = models.CharField(max_length=1)
    st_desc = models.CharField(max_length=30, blank=True, null=True)
    st_st_gp = models.OneToOneField('StGroup', models.DO_NOTHING, db_column='st_st_gp', primary_key=True)
    lastkey = models.DateTimeField()
    lastuser = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'st_grade'
        unique_together = (('st_st_gp', 'st_grade'),)


class StGroup(models.Model):
    st_group = models.CharField(primary_key=True, max_length=1)
    st_desc = models.CharField(max_length=100, blank=True, null=True)
    lastkey = models.DateTimeField()
    lastuser = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'st_group'


class StShape(models.Model):
    st_shape = models.CharField(primary_key=True, max_length=2)
    st_desc = models.CharField(max_length=150, blank=True, null=True)
    st_short = models.CharField(max_length=30, blank=True, null=True)
    lastkey = models.DateTimeField()
    lastuser = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'st_shape'


class StType(models.Model):
    st_st_gp = models.OneToOneField(StGroup, models.DO_NOTHING, db_column='st_st_gp', primary_key=True)
    st_type = models.CharField(max_length=2)
    st_desc = models.CharField(max_length=100, blank=True, null=True)
    st_eng = models.CharField(max_length=100, blank=True, null=True)
    st_fix = models.CharField(max_length=1, blank=True, null=True)
    st_broke = models.IntegerField(blank=True, null=True)
    st_select = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    st_setgp = models.CharField(max_length=2, blank=True, null=True)
    lastkey = models.DateTimeField()
    lastuser = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'st_type'
        unique_together = (('st_st_gp', 'st_type'),)


class Stockpict(models.Model):
    stockid = models.DecimalField(primary_key=True, max_digits=10, decimal_places=0)
    lastuser = models.CharField(max_length=30, blank=True, null=True)
    lastkey = models.DateTimeField()
    img_data_bytea = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stockpict'


class Subpict(models.Model):
    pro_code = models.CharField(max_length=9)
    pro_sub = models.CharField(max_length=2)
    img_data_bytea = models.BinaryField(blank=True, null=True)
    lastuser = models.CharField(max_length=30, blank=True, null=True)
    lastkey = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'subpict'


class Wfcust(models.Model):
    cus_id = models.AutoField(primary_key=True)
    cus_code = models.CharField(unique=True, max_length=10)
    cus_com = models.CharField(max_length=45)
    add1 = models.CharField(max_length=40, blank=True, null=True)
    add2 = models.CharField(max_length=40, blank=True, null=True)
    add3 = models.CharField(max_length=40, blank=True, null=True)
    country = models.CharField(max_length=25, blank=True, null=True)
    telephone = models.CharField(max_length=20, blank=True, null=True)
    fax = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=35, blank=True, null=True)
    ship_com = models.CharField(max_length=45, blank=True, null=True)
    ship_add1 = models.CharField(max_length=45, blank=True, null=True)
    ship_add2 = models.CharField(max_length=45, blank=True, null=True)
    ship_add3 = models.CharField(max_length=45, blank=True, null=True)
    ship_coun = models.CharField(max_length=25, blank=True, null=True)
    ship_tel = models.CharField(max_length=20, blank=True, null=True)
    ship_fax = models.CharField(max_length=20, blank=True, null=True)
    ship_email = models.CharField(max_length=35, blank=True, null=True)
    ship_flag = models.IntegerField()
    ship_acc = models.CharField(max_length=20, blank=True, null=True)
    ship_via = models.CharField(max_length=20, blank=True, null=True)
    cus_fname = models.CharField(max_length=15, blank=True, null=True)
    cus_lname = models.CharField(max_length=30, blank=True, null=True)
    con_tel1 = models.CharField(max_length=20, blank=True, null=True)
    con_fax1 = models.CharField(max_length=20, blank=True, null=True)
    con_mobi1 = models.CharField(max_length=20, blank=True, null=True)
    con_email1 = models.CharField(max_length=35, blank=True, null=True)
    con_fname2 = models.CharField(max_length=15, blank=True, null=True)
    con_lname2 = models.CharField(max_length=30, blank=True, null=True)
    con_tel2 = models.CharField(max_length=20, blank=True, null=True)
    con_fax2 = models.CharField(max_length=20, blank=True, null=True)
    con_mobi2 = models.CharField(max_length=20, blank=True, null=True)
    con_email2 = models.CharField(max_length=35, blank=True, null=True)
    curr_type = models.ForeignKey(CurrType, models.DO_NOTHING, db_column='curr_type')
    col_bank = models.IntegerField()
    cus_g_pr = models.CharField(max_length=10, blank=True, null=True)
    bank_name = models.CharField(max_length=35, blank=True, null=True)
    badd1 = models.CharField(max_length=30, blank=True, null=True)
    badd2 = models.CharField(max_length=30, blank=True, null=True)
    bcountry = models.CharField(max_length=25, blank=True, null=True)
    agen_name = models.CharField(max_length=35, blank=True, null=True)
    aadd1 = models.CharField(max_length=30, blank=True, null=True)
    aadd2 = models.CharField(max_length=30, blank=True, null=True)
    acountry = models.CharField(max_length=25, blank=True, null=True)
    term = models.CharField(max_length=50, blank=True, null=True)
    met_desc = models.CharField(max_length=120, blank=True, null=True)
    colo_met = models.CharField(max_length=120, blank=True, null=True)
    plating = models.CharField(max_length=120, blank=True, null=True)
    acc_part = models.CharField(max_length=120, blank=True, null=True)
    pro_stamp = models.CharField(max_length=120, blank=True, null=True)
    remark1 = models.CharField(max_length=120, blank=True, null=True)
    remark2 = models.CharField(max_length=120, blank=True, null=True)
    tag = models.CharField(max_length=120, blank=True, null=True)
    packing = models.CharField(max_length=120, blank=True, null=True)
    cus_info = models.TextField(blank=True, null=True)
    cus_group = models.CharField(max_length=3, blank=True, null=True)
    add_alloy = models.IntegerField()
    mark_up = models.DecimalField(max_digits=5, decimal_places=2)
    inc_lab = models.IntegerField()
    inc_stn = models.IntegerField()
    inc_dia = models.IntegerField()
    inc_met = models.IntegerField()
    met_loss = models.DecimalField(max_digits=5, decimal_places=2)
    gold_loss = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    silv_loss = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    inv_dis_tp = models.IntegerField()
    inv_dis_rt = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    hallmark = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    sticker = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    mg_sale = models.CharField(max_length=10, blank=True, null=True)
    mg_ref = models.CharField(max_length=10, blank=True, null=True)
    mg_price = models.CharField(max_length=10, blank=True, null=True)
    remarkcus = models.TextField(blank=True, null=True)
    mk_addr = models.TextField(blank=True, null=True)
    mk_country = models.CharField(max_length=40, blank=True, null=True)
    mk_cont = models.CharField(max_length=100, blank=True, null=True)
    mk_cont_em = models.CharField(max_length=100, blank=True, null=True)
    mk_brand = models.CharField(max_length=50, blank=True, null=True)
    mk_metal = models.CharField(max_length=80, blank=True, null=True)
    mk_gems = models.CharField(max_length=80, blank=True, null=True)
    mk_dia = models.CharField(max_length=80, blank=True, null=True)
    mk_shipvia = models.CharField(max_length=20, blank=True, null=True)
    mk_note = models.TextField(blank=True, null=True)
    keydate = models.DateTimeField()
    keyuser = models.CharField(max_length=30)
    lastkey = models.DateTimeField()
    lastuser = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'wfcust'


class WkStation(models.Model):
    wk_station = models.CharField(primary_key=True, max_length=3)
    wk_desc = models.CharField(max_length=30, blank=True, null=True)
    key_date = models.TextField(blank=True, null=True)  # This field type is a guess.
    key_time = models.DateTimeField(blank=True, null=True)
    key_user = models.CharField(max_length=6, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wk_station'


class WkSubstation(models.Model):
    wk_station = models.ForeignKey(WkStation, models.DO_NOTHING, db_column='wk_station', blank=True, null=True)
    wk_substation = models.CharField(max_length=3, blank=True, null=True)
    wk_desc = models.CharField(max_length=30, blank=True, null=True)
    key_date = models.TextField(blank=True, null=True)  # This field type is a guess.
    key_time = models.TextField(blank=True, null=True)  # This field type is a guess.
    key_user = models.CharField(max_length=6, blank=True, null=True)
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'wk_substation'
