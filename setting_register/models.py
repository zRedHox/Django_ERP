from django.db import models

# Create your models here.


class Setting(models.Model):
    setting = models.CharField(primary_key=True, max_length=2)
    description = models.CharField(max_length=80, blank=True, null=True)
    sh_desc = models.CharField(max_length=10, blank=True, null=True)
    lastuser = models.CharField(max_length=30)

    class Meta:
        db_table = 'setting'


class Gfmaster(models.Model):
    pro_code = models.CharField(primary_key=True, max_length=9, unique=True)
    pro_type = models.ForeignKey(
        'ProType', models.DO_NOTHING, db_column='pro_type')
    std_925_wt = models.DecimalField(
        max_digits=10, decimal_places=3, blank=True, null=True)
    mold_wt = models.DecimalField(
        max_digits=10, decimal_places=3, blank=True, null=True)
    mold_metal = models.CharField(max_length=3, blank=True, null=True)
    search_tag1 = models.TextField(blank=True, null=True)
    search_tag2 = models.TextField(blank=True, null=True)
    search_tag3 = models.TextField(blank=True, null=True)
    remark = models.TextField(blank=True, null=True)
    # lastuser = models.CharField(max_length=30)
    surface = models.DecimalField(
        max_digits=10, decimal_places=3, blank=True, null=True)
    # lastkey = models.DateTimeField()
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
    cast_925wt = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True)
    yg_wt = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True)
    yg_castwt = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True)
    cus_yg_wt = models.DecimalField(
        max_digits=10, decimal_places=3, blank=True, null=True)
    wg_wt = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True)
    wg_castwt = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True)
    cus_wg_wt = models.DecimalField(
        max_digits=10, decimal_places=3, blank=True, null=True)
    pt_wt = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True)
    cus_pt_wt = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True)
    si_wt = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True)
    cus_si_wt = models.DecimalField(
        max_digits=10, decimal_places=3, blank=True, null=True)
    br_wt = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True)
    cus_br_wt = models.DecimalField(
        max_digits=10, decimal_places=3, blank=True, null=True)
    ag_wt = models.DecimalField(
        max_digits=10, decimal_places=3, blank=True, null=True)
    sil_chain = models.DecimalField(
        max_digits=10, decimal_places=3, blank=True, null=True)
    true_wt = models.DecimalField(
        max_digits=10, decimal_places=3, blank=True, null=True)
    no_cast = models.DecimalField(
        max_digits=1, decimal_places=0, blank=True, null=True)

    class Meta:
        db_table = 'gfmaster'


class GfSemi(models.Model):
    semi_code = models.CharField(primary_key=True, max_length=30)
    semi_desc = models.CharField(max_length=200, blank=True, null=True)
    # lastkey = models.DateTimeField()
    # lastuser = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'gf_semi'


class GfStockcode(models.Model):
    stockgroup = models.CharField(max_length=100, blank=True)
    stockcode = models.CharField(max_length=19)
    stockdesc = models.CharField(max_length=300, blank=True, null=True)
    unit_qty = models.CharField(max_length=100, blank=True, null=True)
    unit_volume = models.CharField(max_length=100, blank=True, null=True)
    std_wt_gm = models.DecimalField(
        max_digits=10, decimal_places=4, blank=True, null=True)
    std_pr_bt = models.DecimalField(
        max_digits=11, decimal_places=4, blank=True, null=True)
    std_pr_us = models.DecimalField(
        max_digits=10, decimal_places=4, blank=True, null=True)
    std_sale_bt = models.DecimalField(
        max_digits=10, decimal_places=4, blank=True, null=True)
    std_sale_us = models.DecimalField(
        max_digits=10, decimal_places=4, blank=True, null=True)
    std_lb_bt = models.DecimalField(
        max_digits=10, decimal_places=4, blank=True, null=True)
    std_lb_us = models.DecimalField(
        max_digits=10, decimal_places=4, blank=True, null=True)
    # lastkey = models.DateTimeField()
    # lastuser = models.CharField(max_length=30)
    stock_id = models.AutoField(primary_key=True)
    std_unit = models.CharField(max_length=1, blank=True, null=True)
    mt_metal = models.CharField(max_length=100, blank=True)
    eng_desc = models.CharField(max_length=500, blank=True, null=True)
    eng_unit_qty = models.CharField(max_length=50, blank=True, null=True)
    eng_unit_volume = models.CharField(max_length=50, blank=True, null=True)
    max_stock = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True)
    min_stock = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True)
    reorder = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True)
    order_time = models.IntegerField(blank=True, null=True)
    old_code = models.CharField(max_length=19, blank=True, null=True)
    maxmin_fg = models.CharField(max_length=1, blank=True, null=True)
    stock_status = models.CharField(max_length=1, blank=True, null=True)
    keep_stock = models.CharField(max_length=1, blank=True, null=True)
    remark = models.TextField(blank=True, null=True)
    purchase_fg = models.CharField(max_length=1, blank=True, null=True)
    mt_group = models.ForeignKey(
        'MtGroup', models.DO_NOTHING, db_column='mt_group', blank=True, null=True)
    cus_id = models.CharField(max_length=100, blank=True)
    account_type = models.CharField(max_length=1, blank=True, null=True)
    std_lb_time = models.IntegerField(blank=True, null=True)
    lb_remark = models.TextField(blank=True, null=True)
    surface = models.DecimalField(
        max_digits=10, decimal_places=4, blank=True, null=True)
    location = models.CharField(max_length=150, blank=True, null=True)
    sp_s_unit = models.CharField(max_length=30, blank=True, null=True)
    sp_u_conv = models.DecimalField(
        max_digits=6, decimal_places=0, blank=True, null=True)
    have_lb = models.CharField(max_length=1, blank=True, null=True)

    # A unique constraint could not be introspected.
    class Meta:
        managed = False
        db_table = 'gf_stockcode'
        unique_together = (('stockgroup', 'stockcode'),)


class GfMainroute(models.Model):
    rt_main = models.CharField(primary_key=True, max_length=2)
    rt_desc = models.CharField(max_length=40)
    rt_section_fg = models.CharField(max_length=1)
    rt_max_insection = models.IntegerField()
    # lastkey = models.DateTimeField()
    # lastuser = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'gf_mainroute'


class ProType(models.Model):
    pro_type = models.CharField(primary_key=True, max_length=2)
    desc_en = models.CharField(max_length=30, blank=True, null=True)
    unit_en = models.CharField(max_length=3)
    desc_th = models.CharField(max_length=50, blank=True, null=True)
    unit_th = models.CharField(max_length=30)
    # lastkey = models.DateTimeField()
    # lastuser = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'pro_type'


class MtMetal(models.Model):
    mt_metal = models.CharField(primary_key=True, max_length=3)
    mt_desc = models.CharField(max_length=90, blank=True, null=True)
    mt_cal = models.CharField(max_length=3, blank=True, null=True)
    mt_multi = models.DecimalField(
        max_digits=8, decimal_places=2, blank=True, null=True)
    mt_add = models.DecimalField(
        max_digits=8, decimal_places=2, blank=True, null=True)
    mt_pure = models.DecimalField(
        max_digits=8, decimal_places=2, blank=True, null=True)
    mt_alloy = models.DecimalField(
        max_digits=8, decimal_places=2, blank=True, null=True)
    alloy_date = models.DateTimeField(blank=True, null=True)
    old_alloy = models.DecimalField(
        max_digits=8, decimal_places=2, blank=True, null=True)
    mt_show = models.CharField(max_length=3, blank=True, null=True)
    # lastkey = models.DateTimeField()
   # lastuser = models.CharField(max_length=30)
    mt_color = models.ForeignKey(
        'MtColor', models.DO_NOTHING, db_column='mt_color', blank=True, null=True)
    mt_925tf = models.DecimalField(
        max_digits=8, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mt_metal'


class ProMetalbase(models.Model):
    pro_code = models.CharField(max_length=30)
    mt_metal = models.CharField(max_length=30)
    #lastkey = models.DateTimeField()
    #lastuser = models.CharField(max_length=30)
    pro_metal_id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'pro_metalbase'
        unique_together = (('pro_code', 'mt_metal'),)
        constraints = [
            models.UniqueConstraint(
                fields=['pro_code', 'mt_metal'], name='unique_pro_metal')
        ]


class MtColor(models.Model):
    mt_color = models.CharField(primary_key=True, max_length=1)
    mt_desc = models.CharField(max_length=20, blank=True, null=True)
    # lastkey = models.DateTimeField()
    # lastuser = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'mt_color'


class Wfcust(models.Model):
    cus_id = models.AutoField(primary_key=True)
    cus_code = models.CharField(unique=True, max_length=10)
    cus_com = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'wfcust'


class MtGroup(models.Model):
    mt_group = models.CharField(primary_key=True, max_length=2)
    mt_desc = models.CharField(max_length=200, blank=True, null=True)
    # lastkey = models.DateTimeField()
    # lastuser = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'mt_group'


class GfStockgroup(models.Model):
    stockgroup = models.CharField(primary_key=True, max_length=2)
    desc = models.TextField(blank=True, null=True)
    # lastkey = models.DateTimeField()
    # lastuser = models.CharField(max_length=30)
    header_table = models.TextField(blank=True, null=True)
    metal_fg = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'gf_stockgroup'


class Modelpicbytea(models.Model):
    # id = models.AutoField()
    item_name = models.CharField(primary_key=True, max_length=255)
    image_data = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'modelpicbytea'


class ProSpec(models.Model):
    pro_code = models.OneToOneField(
        Gfmaster, models.DO_NOTHING, db_column='pro_code', primary_key=True)
    pd_spec = models.TextField(blank=True, null=True)
    lastkey = models.DateTimeField()
    lastuser = models.CharField(max_length=30)
    rt_main = models.ForeignKey(
        GfMainroute, models.DO_NOTHING, db_column='rt_main')

    class Meta:
        managed = False
        db_table = 'pro_spec'
        unique_together = (('pro_code', 'rt_main'),)


class ProSub(models.Model):
    pro_code = models.CharField(max_length=80, blank=True, null=True)
    pro_sub = models.CharField(max_length=2)
    mt_metal = models.CharField(max_length=3)
    description = models.CharField(max_length=80, blank=True, null=True)
   # lastkey = models.DateTimeField()
    # lastuser = models.CharField(max_length=30)
    pro_sub_id = models.AutoField(primary_key=True)
    metal_check = models.CharField(max_length=1, blank=True, null=True)
    metal_checkdate = models.DateTimeField(blank=True, null=True)
    metal_checkuser = models.CharField(max_length=30, blank=True, null=True)
    routegroup = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pro_sub'
        unique_together = (('pro_code', 'pro_sub'),)


class ProMetal(models.Model):
    pro_code = models.CharField(max_length=80, blank=True, primary_key=True)
    mt_metal = models.CharField(max_length=3)
    sub_metal = models.CharField(max_length=3)
    true_wt = models.DecimalField(
        max_digits=9, decimal_places=3, blank=True, null=True)
    std_conv_wt = models.DecimalField(max_digits=8, decimal_places=2)
    wax_wt = models.DecimalField(
        max_digits=8, decimal_places=2, blank=True, null=True)
    fin_wt = models.DecimalField(
        max_digits=8, decimal_places=2, blank=True, null=True)
    #lastkey = models.DateTimeField()
    #lastuser = models.CharField(max_length=30)
    cus_wt = models.DecimalField(
        max_digits=9, decimal_places=3, blank=True, null=True)
    cast_wt = models.DecimalField(
        max_digits=8, decimal_places=2, blank=True, null=True)
    mt_cast = models.CharField(max_length=1, blank=True, null=True)
    mt_mast = models.CharField(max_length=1, blank=True, null=True)
    stn_set = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pro_metal'
        unique_together = (('pro_code', 'mt_metal', 'sub_metal'),)


class ProRoutegroup(models.Model):
    pro_code = models.CharField(max_length=9)
    routegroup = models.CharField(max_length=2)
    base_sub_id = models.AutoField(primary_key=True)
    # lastkey = models.DateTimeField()
    # lastuser = models.CharField(max_length=30)
    description = models.CharField(max_length=80, blank=True, null=True)
    complete = models.CharField(max_length=1, blank=True, null=True)
    #complete_date = models.DateTimeField(blank=True, null=True)
    #complete_user = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pro_routegroup'
        unique_together = (('pro_code', 'routegroup'),)


class ProSemi(models.Model):
    semi_code = models.CharField(max_length=80, blank=True, primary_key=True)
    semi_char = models.CharField(max_length=1)
    # lastkey = models.DateTimeField()
    # lastuser = models.CharField(max_length=30)
    cast_metal = models.CharField(max_length=3, blank=True, null=True)
    pro_code = models.CharField(max_length=30)
    routegroup = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pro_semi'


class GfRoutecode(models.Model):
    rt_code = models.CharField(max_length=8)
    routecode_id = models.AutoField(primary_key=True)
    rt_desc = models.CharField(max_length=100, blank=True, null=True)
    s_std = models.IntegerField(blank=True, null=True)
    g_std = models.IntegerField(blank=True, null=True)
    rt_unit = models.CharField(max_length=50, blank=True, null=True)
    # lastkey = models.DateTimeField()
    # lastuser = models.CharField(max_length=30)
    rt_spec = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gf_routecode'


class SemiRouteId(models.Model):
    semi_code = models.ForeignKey(
        GfSemi, models.DO_NOTHING, db_column='semi_code')
    semi_route_id = models.AutoField(primary_key=True)
    active = models.CharField(max_length=1)
    # lastkey = models.DateTimeField()
    # lastuser = models.CharField(max_length=30)
    complete = models.CharField(max_length=1, blank=True, null=True)
    complete_date = models.DateTimeField(blank=True, null=True)
    complete_user = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'semi_route_id'


class SemiRoute(models.Model):
    route_seq_id = models.AutoField(primary_key=True)
    semi_route_id = models.CharField(max_length=30, blank=True, null=True)
    routecode_id = models.CharField(max_length=30, blank=True, null=True)
    rt_loop = models.DecimalField(
        max_digits=2, decimal_places=0, blank=True, null=True)
    work_desc = models.TextField(blank=True, null=True)
    route_seq = models.CharField(max_length=6, blank=True, null=True)
    qty = models.CharField(max_length=30, blank=True, null=True)
    u_stdtime_sec = models.DecimalField(
        max_digits=10, decimal_places=0, blank=True, null=True)
    p_realtime_sec = models.DecimalField(
        max_digits=10, decimal_places=0, blank=True, null=True)
    #lastkey = models.DateTimeField()
    #lastuser = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'semi_route'
        unique_together = (('semi_route_id', 'route_seq'),)


class Plating(models.Model):
    plating = models.CharField(primary_key=True, max_length=2)
    description = models.CharField(max_length=200, blank=True, null=True)
    surf = models.CharField(max_length=1)
    # lastkey = models.DateTimeField()
    # lastuser = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'plating'





class ProBom(models.Model):
    pro_sub = models.ForeignKey('ProSub', models.DO_NOTHING)
    stock_id = models.BigIntegerField()
    qty = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True)
    route_seq_id = models.BigIntegerField(blank=True, null=True)
    # lastkey = models.DateTimeField()
    # lastuser = models.CharField(max_length=30)
    bomdata_id = models.AutoField(primary_key=True)
    seq = models.CharField(max_length=3, blank=True, null=True)
    setting = models.ForeignKey(
        'Setting', models.DO_NOTHING, db_column='setting', blank=True, null=True)
    wax_fg = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pro_bom'


class PlatType(models.Model):
    plat_type = models.CharField(primary_key=True, max_length=5)
    description = models.CharField(max_length=200, blank=True, null=True)
    micron = models.DecimalField(max_digits=8, decimal_places=2)
    mt_metal = models.ForeignKey(
        MtMetal, models.DO_NOTHING, db_column='mt_metal', blank=True, null=True)
    plating = models.ForeignKey(
        'Plating', models.DO_NOTHING, db_column='plating')
    surf = models.CharField(max_length=1)
    # lastkey = models.DateTimeField()
    # lastuser = models.CharField(max_length=30)
    remark = models.TextField(blank=True, null=True)
    remarkpr = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'plat_type'


class ProCoat(models.Model):
    pro_code = models.CharField(max_length=30, primary_key=True)
    plat_type = models.CharField(max_length=30)
    # lastkey = models.DateTimeField()
    # lastuser = models.CharField(max_length=30)
    remark = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pro_coat'
        unique_together = (('pro_code', 'plat_type'),)


class ProRingsize(models.Model):
    ring_size = models.CharField(max_length=5)
    # lastkey = models.DateTimeField()
    # lastuser = models.CharField(max_length=30)
    pro_code = models.CharField(max_length=30, primary_key=True)

    class Meta:
        managed = False
        db_table = 'pro_ringsize'
        unique_together = (('pro_code', 'ring_size'),)


class Gfpict(models.Model):
    pro_code = models.CharField(primary_key=True, max_length=9)
    img_data_text = models.TextField(blank=True, null=True)
    img_data_bytea = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gfpict'


class Gfsol(models.Model):
    pro_code = models.CharField(primary_key=True, max_length=9)
    img_data_bytea = models.BinaryField(blank=True, null=True)
    # lastkey = models.DateTimeField()
    # lastuser = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'gfsol'


class StBott(models.Model):
    st_bott = models.CharField(primary_key=True, max_length=2)
    st_desc = models.CharField(max_length=100, blank=True, null=True)
    # lastkey = models.DateTimeField()
    # lastuser = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'st_bott'


class StFancy(models.Model):
    st_new = models.CharField(primary_key=True, max_length=15)
    st_newold = models.CharField(max_length=15, blank=True, null=True)
    st_old = models.CharField(max_length=5, blank=True, null=True)
    st_shape = models.ForeignKey(
        'StShape', models.DO_NOTHING, db_column='st_shape', blank=True, null=True)
    st_width = models.DecimalField(
        max_digits=7, decimal_places=2, blank=True, null=True)
    st_long = models.DecimalField(
        max_digits=7, decimal_places=2, blank=True, null=True)
    st_front = models.ForeignKey(
        'StFront', models.DO_NOTHING, db_column='st_front', blank=True, null=True)
    st_bott = models.ForeignKey(
        StBott, models.DO_NOTHING, db_column='st_bott', blank=True, null=True)
    st_h_font = models.DecimalField(
        max_digits=7, decimal_places=2, blank=True, null=True)
    st_h_bott = models.DecimalField(
        max_digits=7, decimal_places=2, blank=True, null=True)
    st_h_line = models.DecimalField(
        max_digits=7, decimal_places=2, blank=True, null=True)
    st_h_cross = models.DecimalField(
        max_digits=7, decimal_places=2, blank=True, null=True)
    st_remark = models.TextField(blank=True, null=True)
    # lastkey = models.DateTimeField()
    # lastuser = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'st_fancy'


class StFront(models.Model):
    st_front = models.CharField(primary_key=True, max_length=2)
    st_desc = models.CharField(max_length=100, blank=True, null=True)
    # lastkey = models.DateTimeField()
    # lastuser = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'st_front'


class StGrade(models.Model):
    st_grade = models.CharField(max_length=1)
    st_desc = models.CharField(max_length=30, blank=True, null=True)
    st_st_gp = models.OneToOneField(
        'StGroup', models.DO_NOTHING, db_column='st_st_gp', primary_key=True)
    # lastkey = models.DateTimeField()
    # lastuser = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'st_grade'
        unique_together = (('st_st_gp', 'st_grade'),)


class StGroup(models.Model):
    st_group = models.CharField(primary_key=True, max_length=1)
    st_desc = models.CharField(max_length=100, blank=True, null=True)
    # lastkey = models.DateTimeField()
    # lastuser = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'st_group'


class StShape(models.Model):
    st_shape = models.CharField(primary_key=True, max_length=2)
    st_desc = models.CharField(max_length=150, blank=True, null=True)
    st_short = models.CharField(max_length=30, blank=True, null=True)
    # lastkey = models.DateTimeField()
    # lastuser = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'st_shape'


class StType(models.Model):
    st_st_gp = models.CharField(max_length=4)
    st_type = models.CharField(max_length=2, primary_key=True)
    st_desc = models.CharField(max_length=100, blank=True, null=True)
    st_eng = models.CharField(max_length=100, blank=True, null=True)
    st_fix = models.CharField(max_length=1, blank=True, null=True)
    st_broke = models.IntegerField(blank=True, null=True)
    st_select = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True)
    st_setgp = models.CharField(max_length=2, blank=True, null=True)
    # lastkey = models.DateTimeField()
    # lastuser = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'st_type'
        unique_together = (('st_st_gp', 'st_type'),)


class Enamel(models.Model):
    pantone = models.CharField(primary_key=True, max_length=10)
    description = models.CharField(max_length=100)
    #lastkey = models.DateTimeField()
    #lastuser = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'enamel'

class ProEna(models.Model):
    pro_sub_id = models.CharField(max_length=100, primary_key=True)
    pantone = models.CharField(max_length=100)
    pn_no = models.CharField(max_length=3)
    #lastkey = models.DateTimeField()
    #lastuser = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'pro_ena'
        unique_together = (('pro_sub_id', 'pantone', 'pn_no'),)


class ProMetalbom(models.Model):
    pro_metal_id = models.CharField(primary_key=True,max_length=100)
    stock_id = models.CharField(max_length=100)
    qty = models.DecimalField(max_digits=10, decimal_places=2)
    route_seq_id = models.IntegerField(blank=True, null=True)
    bomdata_id = models.CharField(models.DO_NOTHING,max_length=100)
    semi_char = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pro_metalbom'


class Subpict(models.Model):
    pro_code = models.CharField(max_length=9,primary_key=True)
    pro_sub = models.CharField(max_length=2)
    img_data_bytea = models.BinaryField(blank=True, null=True)
    #lastuser = models.CharField(max_length=30, blank=True, null=True)
    #lastkey = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'subpict'


