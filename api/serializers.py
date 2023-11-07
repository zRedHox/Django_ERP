from rest_framework import serializers
from setting_register.models import Setting, Gfmaster, GfSemi, GfStockcode, GfMainroute, ProType, \
    ProMetalbase, MtMetal, MtColor, Wfcust, MtGroup, GfStockgroup, Modelpicbytea, Gfpict, \
        ProSpec, ProSub, ProMetal, ProRoutegroup, ProSemi, GfRoutecode, SemiRouteId, ProMetalbom, \
    ProBom, ProCoat, PlatType, ProRingsize, StBott, StFancy, StFront, StGrade, StGroup, StShape, \
    StType, ProEna, Enamel, ProMetalbom, Subpict, SemiRoute
    
    


class SettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Setting
        fields = '__all__'


class GfmasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gfmaster
        fields = '__all__'


class GfSemiSerializer(serializers.ModelSerializer):
    class Meta:
        model = GfSemi
        fields = '__all__'


class GfStockcodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = GfStockcode
        fields = '__all__'


class GfMainrouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = GfMainroute
        fields = '__all__'


class ProTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProType
        fields = '__all__'


class ProMetalbaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProMetalbase
        fields = '__all__'


class MtMetalSerializer(serializers.ModelSerializer):
    class Meta:
        model = MtMetal
        fields = '__all__'


class MtColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = MtColor
        fields = '__all__'


class WfcustSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wfcust
        fields = '__all__'


class MtGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = MtGroup
        fields = '__all__'


class GfStockgroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = GfStockgroup
        fields = '__all__'


class ModelpicbyteaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Modelpicbytea
        fields = '__all__'
# Gfpict


class GfpictSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gfpict
        fields = '__all__'


class ProSpecSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProSpec
        fields = '__all__'


class ProSubSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProSub
        fields = '__all__'


class ProMetalSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProMetal
        fields = '__all__'


# ProRoutegroup
class ProRoutegroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProRoutegroup
        fields = '__all__'


# ProSemi
class ProSemiSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProSemi
        fields = '__all__'

# GfRoutecode


class GfRoutecodeSerializer(serializers.ModelSerializer):

    class Meta:
        model = GfRoutecode
        fields = '__all__'

# SemiRouteId


class SemiRouteIdSerializer(serializers.ModelSerializer):

    class Meta:
        model = SemiRouteId
        fields = '__all__'


class ProMetalbomSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProMetalbom
        fields = '__all__'


class ProBomSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProBom
        fields = '__all__'

# ProCoat


class ProCoatSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProCoat
        fields = '__all__'

# PlatType


class PlatTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlatType
        fields = '__all__'

# ProRingsize
class ProRingsizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProRingsize
        fields = '__all__'


class SemiRouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = SemiRoute
        fields = '__all__'


class JoinedSemiSerializer(serializers.ModelSerializer):
    semi_code = serializers.CharField()
    semi_desc = serializers.SerializerMethodField()
    semi_char = serializers.CharField()
    routegroup = serializers.CharField()
    gf_semi = GfSemiSerializer(many=True, read_only=True)

    def get_semi_desc(self, obj):
        gf_semi = GfSemi.objects.filter(semi_code=obj.semi_code).first()
        if gf_semi:
            return gf_semi.semi_desc
        else:
            return None

    class Meta:
        model = ProSemi
        fields = ('semi_code', 'semi_desc', 'semi_char',
                  'routegroup', 'gf_semi', 'pro_code')


# ===========================================================================
#  *                                 INFO
#    ใช้ serializers.CharField() เมื่อค่านั้นมีอยู่แล้วในตัวของมันเองไม่ต้อง join จากใคร
#    ใช้ serializers.SerializerMethodFiled() ถ้าค่านั้นต้องมาจาก return ของฟังชั่นนั้นๆ เช่น ค่าของ pro_code จะมาจากการ return ค่าจาก def get_pro_code
#
#
# ===========================================================================


class JoinedProMetalBomSerializer(serializers.ModelSerializer):
    # * INFO ใช้ serializers.CharField() เมื่อค่านั้นมีอยู่แล้วในตัวของมันเองไม่ต้อง join จากใคร
    stock_id = serializers.CharField()
    stockgroup = serializers.SerializerMethodField()
    stockcode = serializers.SerializerMethodField()
    # * INFO ใช้ serializers.SerializerMethodFiled() ถ้าค่านี้ต้องมาจาก return ของฟังชั่นนั้นๆ เช่น ค่าของ stockdesc จะมาจากการ return ค่าจาก def get_stockdesc
    stockdesc = serializers.SerializerMethodField()
    mtmetal = serializers.SerializerMethodField()
    qty = serializers.CharField()
    unit_qty = serializers.SerializerMethodField()
    route_seq_id = serializers.CharField()
    # cus_com = serializers.SerializerMethodField()
    pro_metal_id = serializers.CharField()
    # * INFO ใช้ serializers.SerializerMethodFiled() ถ้าค่านี้ต้องมาจาก return ของฟังชั่นนั้นๆ เช่น ค่าของ pro_code จะมาจากการ return ค่าจาก def get_pro_code
    pro_code = serializers.SerializerMethodField()
    gf_stockcode = GfStockcodeSerializer(many=True, read_only=True)
    pro_metalbase = ProMetalbaseSerializer(many=True, read_only=True)

# ================================================
#  *                    INFO
#      function  ข้างล่างนี้
#    เป็นการเอาค่าแต่ละ table ไป join หาค่าที่ต้องมา
#
#    เช่น def get_stockcode ต้องการหาค่า stockcode
#    เอา stock_id ของ Prometalbom = obj.stock_id (obj.stock_id คือ stock_id ของ GfStockcode)
#    ถ้าเจอ ให้คืนค่า stockcode ที่อยู่ใน gf_stockcode
# ================================================

    def get_stockcode(self, obj):
        gf_stockcodes = GfStockcode.objects.filter(stock_id=obj.stock_id)
        if gf_stockcodes:
            return [gf_stockcode.stockcode for gf_stockcode in gf_stockcodes]
        else:
            return None

    def get_mtmetal(self, obj):
        gf_stockcode = GfStockcode.objects.filter(
            stock_id=obj.stock_id).first()
        if gf_stockcode:
            return gf_stockcode.mt_metal
        else:
            return ''

    def get_unit_qty(self, obj):
        gf_stockcode = GfStockcode.objects.filter(
            stock_id=obj.stock_id).first()
        if gf_stockcode:
            return gf_stockcode.unit_qty
        else:
            return None

    def get_pro_code(self, obj):
        pro_metalbase = ProMetalbase.objects.filter(
            pro_metal_id=obj.pro_metal_id).first()
        if pro_metalbase:
            return pro_metalbase.pro_code
        else:
            return None

    def get_stockgroup(self, obj):
        gf_stockcode = GfStockcode.objects.filter(
            stock_id=obj.stock_id).first()
        if gf_stockcode:
            return gf_stockcode.stockgroup
        else:
            return None

    def get_stockdesc(self, obj):
        gf_stockcode = GfStockcode.objects.filter(
            stock_id=obj.stock_id).first()
        if gf_stockcode:
            return gf_stockcode.stockdesc
        else:
            return None

    class Meta:
        model = ProMetalbom
        fields = ('stock_id', 'stockcode', 'stockgroup', 'mtmetal', 'route_seq_id', 'qty',
                  'unit_qty',  'stockdesc', 'pro_metal_id', 'gf_stockcode', 'pro_code', 'pro_metalbase')


class JoinBomlist(serializers.ModelSerializer):
    pro_sub_id = serializers.CharField()
    stock_id = serializers.CharField()
    stockgroup = serializers.SerializerMethodField()
    stockcode = serializers.SerializerMethodField()
    stockdesc = serializers.SerializerMethodField()
    mt_metal = serializers.SerializerMethodField()
    qty = serializers.CharField()
    unit_qty = serializers.SerializerMethodField()
    route_seq_id = serializers.CharField()
    bomdata_id = serializers.CharField()
    seq = serializers.CharField()
    setting = serializers.CharField()
    wax_fg = serializers.CharField()
    gf_stockcodes = GfStockcodeSerializer(many=True, read_only=True)
    wfcust = WfcustSerializer(many=True, read_only=True)
    cus_com = serializers.SerializerMethodField()

    def get_stockgroup(self, obj):
        gf_stockcodes = GfStockcode.objects.filter(
            stock_id=obj.stock_id).first()   #obj.stock_id เอาstock_id ของ Probom ไปjoin กับ stock_id ใน GfStockcode
        if gf_stockcodes:
            return gf_stockcodes.stockgroup
        else:
            return None

    def get_stockcode(self, obj):
        gf_stockcodes = GfStockcode.objects.filter(
            stock_id=obj.stock_id).first()
        if gf_stockcodes:
            return gf_stockcodes.stockcode
        else:
            return None

    def get_stockdesc(self, obj):
        gf_stockcodes = GfStockcode.objects.filter(
            stock_id=obj.stock_id).first()
        if gf_stockcodes:
            return gf_stockcodes.stockdesc
        else:
            return None

    def get_mt_metal(self, obj):
        gf_stockcodes = GfStockcode.objects.filter(
            stock_id=obj.stock_id).first()
        if gf_stockcodes:
            return gf_stockcodes.mt_metal
        else:
            return ''

    def get_unit_qty(self, obj):
        gf_stockcodes = GfStockcode.objects.filter(
            stock_id=obj.stock_id).first()
        if gf_stockcodes:
            return gf_stockcodes.unit_qty
        else:
            return None

    def get_cus_com(self, obj):
        gf_stockcodes = GfStockcode.objects.filter(stock_id=obj.stock_id)
        if gf_stockcodes:
            wfcust = Wfcust.objects.filter(
                cus_id=gf_stockcodes[0].cus_id).first()
            if wfcust:
                return wfcust.cus_com
        return None

    class Meta:
        model = ProBom
        fields = ('pro_sub_id', 'stock_id', 'stockgroup', 'stockcode', 'stockdesc', 'mt_metal', 'qty', 'unit_qty',
                  'route_seq_id', 'bomdata_id', 'seq', 'setting', 'wax_fg', 'gf_stockcodes', 'wfcust', 'cus_com')

# ================================= StBott ================================
class StBottSerializer(serializers.ModelSerializer):
    class Meta:
        model = StBott
        fields = '__all__'


# ================================= StFancy ================================
class StFancySerializer(serializers.ModelSerializer):
    class Meta:
        model = StFancy
        fields = '__all__'

# ================================= StFront ================================
class StFrontSerializer(serializers.ModelSerializer):
    class Meta:
        model = StFront
        fields = '__all__'

# ================================= StGrade ================================
class StGradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = StGrade
        fields = '__all__'

# ================================= StGroup ================================
class StGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = StGroup
        fields = '__all__'


# ================================= StShape ================================
class StShapeSerializer(serializers.ModelSerializer):
    class Meta:
        model = StShape
        fields = '__all__'

# ================================= StType ================================
class StTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = StType
        fields = '__all__'


# ================================= ProEna ================================
class ProEnaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProEna
        fields = '__all__'

# ================================= Enamel ================================


class EnamelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enamel
        fields = '__all__'

# ================================= ProMetalbom ================================

class ProMetalbomSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProMetalbom
        fields = '__all__'



#================================= subpict ================================

class SubpictSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subpict
        fields = '__all__'






