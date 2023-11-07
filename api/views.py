# ===========================================================================
#  *                                 README
#    *        ลง extension "better comment" ก่อนแล้วจะเห็นสีที่ comment ไว้
#
#
#
# ===========================================================================


from rest_framework.response import Response
from rest_framework.decorators import api_view
from setting_register.models import Setting, Gfmaster, GfSemi, GfStockcode, GfMainroute, ProType, \
    ProMetalbase, MtMetal, MtColor, Wfcust, MtGroup, GfStockgroup, Modelpicbytea, ProSpec, ProSub,\
          ProMetal, ProRoutegroup, ProSemi, GfRoutecode, SemiRouteId, ProMetalbom, ProBom, ProCoat, \
    PlatType, ProRingsize, Gfpict, Gfsol, StType, StFancy, StFront, StShape, StBott, StGrade, ProEna, Enamel,\
    ProMetalbom, Subpict, SemiRoute
from .serializers import SettingSerializer, GfmasterSerializer, GfSemiSerializer, \
    GfStockcodeSerializer, GfMainrouteSerializer, ProTypeSerializer, ProMetalbaseSerializer,\
          MtMetalSerializer, MtColorSerializer, WfcustSerializer, MtGroupSerializer, GfStockgroupSerializer, \
            ModelpicbyteaSerializer, ProSpecSerializer, ProSubSerializer, ProMetalSerializer, \
                ProRoutegroupSerializer, ProSemiSerializer, GfRoutecodeSerializer, SemiRouteIdSerializer,\
                      JoinedSemiSerializer, JoinedProMetalBomSerializer, JoinBomlist, ProCoatSerializer, \
    PlatTypeSerializer, ProRingsizeSerializer, StTypeSerializer, StFancySerializer, StFrontSerializer, \
    StShapeSerializer, StBottSerializer, StGradeSerializer, ProEnaSerializer, EnamelSerializer, ProMetalbomSerializer, \
    SubpictSerializer, SemiRouteSerializer

from rest_framework import status, generics
from rest_framework.views import APIView
from django.http import HttpResponse, Http404
from django.db.models import F, Value, CharField, Case, When, Subquery, OuterRef, Q
from django.db.models.functions import Concat
from rest_framework import generics
from django.core.paginator import Paginator


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
# ! id รับมาจากช่องให้ใส่ อาจเป็นรหัสการฝัง , เลขโมเดล , มักเป็น primary key ของตาราง
def handleData(request, id=None):
    # GET request
    if request.method == 'GET':  # !  ถ้ามี request GET
        if id is not None:  # ! ID ไม่ใช่ค่าว่าง
            # ! เก็บข้อมูลที่หาเจอจาก primary key เก็บใน settingno  คล้ายๆ query
            settingno = Setting.objects.filter(pk=id).first()
            if settingno is None:
                # ! ถ้าหาไม่เจอ return not found
                return Response(status=status.HTTP_404_NOT_FOUND)
            serializer = SettingSerializer(settingno)
            return Response(serializer.data)
        else:
            settingno = Setting.objects.all()  # ! ถ้าเจอ เก็บข้อมูลทั้งหมดใน settingno
            # ! ส่ง settingnoไปทำ serializer เพื่อแสดงผล  ตัว Seriallizer คือตัวที่บอกว่าจะแสดง field ไหนบ้าง ไปดูในไฟล์ serializers.py
            serializer = SettingSerializer(settingno, many=True)
            return Response(serializer.data)

    # POST request
    elif request.method == 'POST':  # ! เพิ่มข้อมูล
        serializer = SettingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # PUT request
    elif request.method == 'PUT':  # ! อัพเดท
        settingno = Setting.objects.filter(pk=id).first()
        if settingno is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = SettingSerializer(settingno, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # DELETE request
    elif request.method == 'DELETE':  # ! ลบ
        settingno = Setting.objects.filter(pk=id).first()
        if settingno is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        settingno.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# --------------------------------
# gfmaster
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def handleDataGfmaster(request, id=None):
    # GET request
    if request.method == 'GET':
        if id is not None:
            gfmaster_data = Gfmaster.objects.filter(pk=id).first()
            if gfmaster_data is None:
                return Response(status=status.HTTP_404_NOT_FOUND)
            serializer = GfmasterSerializer(gfmaster_data)
            return Response(serializer.data)
        else:
            # Get the page number from the request query parameters, default to 1 if not provided
            page_number = int(request.GET.get('page', 1))
            gfmaster_data = Gfmaster.objects.all()
            # Paginate the data
            paginator = Paginator(gfmaster_data, 20)  # 20 records per page
            page_obj = paginator.get_page(page_number)
            serializer = GfmasterSerializer(page_obj, many=True)
            return Response(serializer.data)

    # POST request
    elif request.method == 'POST':
        serializer = GfmasterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # PUT request
    elif request.method == 'PUT':
        gfmaster_data = Gfmaster.objects.filter(pk=id).first()
        if gfmaster_data is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = GfmasterSerializer(gfmaster_data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # DELETE request
    elif request.method == 'DELETE':
        gfmaster_data = Gfmaster.objects.filter(pk=id).first()
        if gfmaster_data is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        gfmaster_data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# ---------------------------------
# GfSemi

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def handleDataGfSemi(request, id=None):
    # GET request
    if request.method == 'GET':
        if id is not None:
            GfSemi_data = GfSemi.objects.filter(pk=id).first()
            if GfSemi_data is None:
                return Response(status=status.HTTP_404_NOT_FOUND)
            serializer = GfSemiSerializer(GfSemi_data)
            return Response(serializer.data)
        else:
            GfSemi_data = GfSemi.objects.all()
            serializer = GfSemiSerializer(GfSemi_data, many=True)
            return Response(serializer.data)

    # POST request
    elif request.method == 'POST':
        serializer = GfSemiSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # PUT request
    elif request.method == 'PUT':
        GfSemi_data = Gfmaster.objects.filter(pk=id).first()
        if GfSemi_data is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = GfSemiSerializer(GfSemi_data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # DELETE request
    elif request.method == 'DELETE':
        GfSemi_data = GfSemi.objects.filter(pk=id).first()
        if GfSemi_data is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        GfSemi_data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# ---------------------------------
# GfStockcode

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def handleDataGfStockcode(request, id=None):
    # GET request
    if request.method == 'GET':
        if id is not None:
            GfStockcode_data = GfStockcode.objects.filter(pk=id).first()
            if GfStockcode_data is None:
                return Response(status=status.HTTP_404_NOT_FOUND)
            serializer = GfStockcodeSerializer(GfStockcode_data)
            return Response(serializer.data)
        else:
            GfStockcode_data = GfStockcode.objects.all()
            serializer = GfStockcodeSerializer(GfStockcode_data, many=True)
            return Response(serializer.data)


# ---------------------------------
# GfMainroute

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def handleDataGfMainroute(request, id=None):
    # GET request
    if request.method == 'GET':
        if id is not None:
            GfMainroute_data = GfMainroute.objects.filter(pk=id).first()
            if GfMainroute_data is None:
                return Response(status=status.HTTP_404_NOT_FOUND)
            serializer = GfMainrouteSerializer(GfMainroute_data)
            return Response(serializer.data)
        else:
            GfMainroute_data = GfMainroute.objects.all()
            serializer = GfMainrouteSerializer(GfMainroute_data, many=True)
            return Response(serializer.data)


# ---------------------------------
# ProType

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def handleDataProType(request, id=None):
    # GET request
    if request.method == 'GET':
        if id is not None:
            ProType_data = ProType.objects.filter(pk=id).first()
            if ProType_data is None:
                return Response(status=status.HTTP_404_NOT_FOUND)
            serializer = ProTypeSerializer(ProType_data)
            return Response(serializer.data)
        else:
            ProType_data = ProType.objects.all()
            serializer = ProTypeSerializer(ProType_data, many=True)
            return Response(serializer.data)


# ---------------------------------
# ProMetalbase

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def handleData_Metalbase(request, pro_code=None,id2=None):
    # GET request
    if request.method == 'GET':
        if pro_code is not None:
            ProMetalbase_data = ProMetalbase.objects.filter(
                pro_code=pro_code, mt_metal=id2).first()
            if ProMetalbase_data is None:
                return Response(status=status.HTTP_404_NOT_FOUND)
            serializer = ProMetalbaseSerializer(ProMetalbase_data)
            return Response(serializer.data)
        else:
            ProMetalbase_data = ProType.objects.all()
            serializer = ProMetalbaseSerializer(ProMetalbase_data, many=True)
            return Response(serializer.data)


# ---------------------------------
# MtMetal

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def handleData_MtMetal(request, id=None):
    # GET request
    if request.method == 'GET':
        if id is not None:
            MtMetal_data = MtMetal.objects.filter(pk=id).first()
            if MtMetal_data is None:
                return Response(status=status.HTTP_404_NOT_FOUND)
            serializer = MtMetalSerializer(MtMetal_data)
            return Response(serializer.data)
        else:
            MtMetal_data = MtMetal.objects.all()
            serializer = MtMetalSerializer(MtMetal_data, many=True)
            return Response(serializer.data)


# ---------------------------------
# MtColor

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def handleData_MtColor(request, id=None):
    # GET request
    if request.method == 'GET':
        if id is not None:
            MtColor_data = MtColor.objects.filter(pk=id).first()
            if MtColor_data is None:
                return Response(status=status.HTTP_404_NOT_FOUND)
            serializer = MtColorSerializer(MtColor_data)
            return Response(serializer.data)
        else:
            MtColor_data = MtColor.objects.all()
            serializer = MtColorSerializer(MtColor_data, many=True)
            return Response(serializer.data)


# ---------------------------------
# Wfcust

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def handleData_Wfcust(request, id=None):
    # GET request
    if request.method == 'GET':
        if id is not None:
            Wfcust_data = Wfcust.objects.filter(pk=id).first()
            if Wfcust_data is None:
                return Response(status=status.HTTP_404_NOT_FOUND)
            serializer = WfcustSerializer(Wfcust_data)
            return Response(serializer.data)
        else:
            Wfcust_data = Wfcust.objects.all()
            serializer = WfcustSerializer(Wfcust_data, many=True)
            return Response(serializer.data)


# ---------------------------------
# MtGroup

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def handleData_MtGroup(request, id=None):
    # GET request
    if request.method == 'GET':
        if id is not None:
            MtGroup_data = MtGroup.objects.filter(pk=id).first()
            if MtGroup_data is None:
                return Response(status=status.HTTP_404_NOT_FOUND)
            serializer = MtGroupSerializer(MtGroup_data)
            return Response(serializer.data)
        else:
            MtGroup_data = MtGroup.objects.all()
            serializer = MtGroupSerializer(MtGroup_data, many=True)
            return Response(serializer.data)


# ---------------------------------
# GfStockgroup

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def handleData_GfStockgroup(request, id=None):
    # GET request
    if request.method == 'GET':
        if id is not None:
            GfStockgroup_data = GfStockgroup.objects.filter(pk=id).first()
            if GfStockgroup_data is None:
                return Response(status=status.HTTP_404_NOT_FOUND)
            serializer = GfStockgroupSerializer(GfStockgroup_data)
            return Response(serializer.data)
        else:
            GfStockgroup_data = GfStockgroup.objects.all()
            serializer = GfStockgroupSerializer(GfStockgroup_data, many=True)
            return Response(serializer.data)


# ---------------------------------
# modelpic
# Modelpicbytea

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def handleData_Modelpicbytea(request, id=None):
    # GET request
    if request.method == 'GET':
        if id is not None:
            Modelpicbytea_data = Modelpicbytea.objects.filter(pk=id).first()
            if Modelpicbytea_data is None:
                return Response(status=status.HTTP_404_NOT_FOUND)
            serializer = ModelpicbyteaSerializer(Modelpicbytea_data)
            return Response(serializer.data)
        else:
            Modelpicbytea_data = Modelpicbytea.objects.all()
            serializer = ModelpicbyteaSerializer(Modelpicbytea_data, many=True)
            return Response(serializer.data)


class ImageAPIView(APIView):
    def get(self, request, pk):
        image = Gfpict.objects.get(pk=pk)
        image_data = image.img_data_bytea
        response = HttpResponse(content=image_data, content_type='image/jpeg')
        response['Content-Disposition'] = f'inline; filename="{image.pro_code}"'
        return response


class ImageAPIView_gfsol(APIView):
    def get(self, request, pk):
        try:
            image = Gfsol.objects.get(pk=pk)
            image_data = image.img_data_bytea
            response = HttpResponse(
                content=image_data, content_type='image/jpeg')
            response['Content-Disposition'] = f'inline; filename="{image.pro_code}"'
            return response
        except Gfsol.DoesNotExist:
            # Log the message
            print("gfsol number not found")

            # Raise Http404 exception
            raise Http404("gfsol number not found")



# ---------------------------------
# pro_spec  แบบ handle many to many

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def handleData_ProSpec(request, id=None):
    # GET request
    if request.method == 'GET':
        if id is not None:
            ProSpec_data = ProSpec.objects.filter(pk=id)
            if not ProSpec_data:
                return Response(status=status.HTTP_404_NOT_FOUND)
            serializer = ProSpecSerializer(ProSpec_data, many=True)
            return Response(serializer.data)
        else:
            ProSpec_data = ProSpec.objects.all()
            serializer = ProSpecSerializer(ProSpec_data, many=True)
            return Response(serializer.data)


# ---------------------------------
# prosub  แบบ handle many to many  #work

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def handleData_ProSub(request, id=None):
    # GET request
    if request.method == 'GET':
        if id is not None:
            ProSub_data = ProSub.objects.filter(pro_code=id)
            if not ProSub_data:
                return Response(status=status.HTTP_404_NOT_FOUND)
            serializer = ProSubSerializer(ProSub_data, many=True)
            return Response(serializer.data)
        else:
            ProSub_data = ProSub.objects.all()
            serializer = ProSubSerializer(ProSub_data, many=True)
            return Response(serializer.data)
#routebyprosub      
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def handleData_routeProSub(request, id=None,route=None):
    # GET request
    if request.method == 'GET':
        if id is not None:
            ProSub_data = ProSub.objects.filter(pro_code=id,routegroup=route)
            if not ProSub_data:
                return Response(status=status.HTTP_404_NOT_FOUND)
            serializer = ProSubSerializer(ProSub_data, many=True)
            return Response(serializer.data)
        else:
            ProSub_data = ProSub.objects.all()
            serializer = ProSubSerializer(ProSub_data, many=True)
            return Response(serializer.data)
# ---------------------------------
# prometal


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def handleData_ProMetal(request, id=None, mt_metal=None):
    # GET request
    if request.method == 'GET':
        if id is not None:
            ProMetal_data = ProMetal.objects.filter(
                pro_code=id, mt_metal=mt_metal)
            if not ProMetal_data:
                return Response(status=status.HTTP_404_NOT_FOUND)
            serializer = ProMetalSerializer(ProMetal_data, many=True)
            return Response(serializer.data)
        else:
            ProMetal_data = ProMetal.objects.all()
            serializer = ProMetalSerializer(ProMetal_data, many=True)
            return Response(serializer.data)

# ---------------------------------------
# pro_route_group


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def handleData_ProRouteGroup(request, id=None):
    # GET request
    if request.method == 'GET':
        if id is not None:
            ProRoutegroup_data = ProRoutegroup.objects.filter(pro_code=id)
            if not ProRoutegroup_data:
                return Response(status=status.HTTP_404_NOT_FOUND)
            serializer = ProRoutegroupSerializer(ProRoutegroup_data, many=True)
            return Response(serializer.data)
        else:
            ProRoutegroup_data = ProRoutegroup.objects.all()
            serializer = ProRoutegroupSerializer(ProRoutegroup_data, many=True)
            return Response(serializer.data)


# ---------------------------------------
# ProSemi
# ProSemiSerializer

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def handleData_ProSemi(request, id=None,routegroup=None):
    # GET request
    if request.method == 'GET':
        if id is not None:
            ProSemi_data = ProSemi.objects.filter(pro_code=id,routegroup=routegroup)
            if not ProSemi_data:
                return Response(status=status.HTTP_404_NOT_FOUND)
            serializer = ProSemiSerializer(ProSemi_data, many=True)
            return Response(serializer.data)
        else:
            ProSemi_data = ProSemi.objects.all()
            serializer = ProSemiSerializer(ProSemi_data, many=True)
            return Response(serializer.data)

# -------------------------------------------------
# GfRoutecodeSerializer
# GfRoutecode


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def handleData_GfRoutecode(request, id=None):
    # GET request
    if request.method == 'GET':
        if id is not None:
            GfRoutecode_data = GfRoutecode.objects.filter(routecode_id=id)
            if not GfRoutecode_data:
                return Response(status=status.HTTP_404_NOT_FOUND)
            serializer = GfRoutecodeSerializer(GfRoutecode_data, many=True)
            return Response(serializer.data)
        else:
            GfRoutecode_data = GfRoutecode.objects.all()
            serializer = GfRoutecodeSerializer(GfRoutecode_data, many=True)
            return Response(serializer.data)

# -----------------------------------------------------------
# SemiRouteId
# SemiRouteIdSerializer


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def handleData_SemiRouteId(request, id=None):
    # GET request
    if request.method == 'GET':
        if id is not None:
            SemiRouteId_data = SemiRouteId.objects.filter(semi_code=id)
            if not SemiRouteId_data:
                return Response(status=status.HTTP_404_NOT_FOUND)
            serializer = SemiRouteIdSerializer(SemiRouteId_data, many=True)
            return Response(serializer.data)
        else:
            SemiRouteId_data = SemiRouteId.objects.all()
            serializer = SemiRouteIdSerializer(SemiRouteId_data, many=True)
            return Response(SemiRouteId_data.data)


@api_view(['GET'])
def handleData_SemiRoute(request,id=None):
    #Get request
    if request.method == 'GET':
        if id is not None:
            SemiRoute_data = SemiRoute.objects.filter(semi_route_id = id)
            if not SemiRoute_data:
                return Response(status=status.HTTP_404_NOT_FOUND)
            serializer = SemiRouteSerializer(SemiRoute_data,many=True)
            return Response(serializer.data)
        else:
            SemiRoute_data = SemiRoute_data.objects.all()
            serializer = SemiRouteSerializer(SemiRoute_data,many=True)
            return Response(SemiRoute_data.data)

# -----------------------------------------------
# * INFO join Semi
# JoinedSemiSerializer


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def pro_semi_list(request):
    if request.method == 'GET':
        queryset = ProSemi.objects.all()
        serializer = JoinedSemiSerializer(queryset, many=True)
        return Response(serializer.data)

# -----------------------------------------------
# * INFO seach Prosemi_Table ที่ join ไว้แล้ว กับ gf_semi


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def handleData_Join_ProSemi(request, id=None):
    # GET request
    if request.method == 'GET':
        if id is not None:
            join_ProSemi_data = ProSemi.objects.filter(pro_code=id)
            if not join_ProSemi_data:
                return Response(status=status.HTTP_404_NOT_FOUND)
            serializer = JoinedSemiSerializer(join_ProSemi_data, many=True)
            return Response(serializer.data)
        else:
            join_ProSemi_data = ProSemi.objects.all()
            serializer = JoinedSemiSerializer(join_ProSemi_data, many=True)
            return Response(join_ProSemi_data.data)


# --------------------------------------------
# * join pro_bomb
# joinedprobombserializers

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def pro_metalbomb_list(request):
    if request.method == 'GET':
        queryset = ProMetalbom.objects.all()
        serializer = JoinedProMetalBomSerializer(queryset, many=True)
        return Response(serializer.data)


# -----------------------------------------------
# * INFO seach JoinedProMetalBomSerializer ที่ join ไว้แล้ว
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def handleData_Join_ProMetalBom(request, id=None):
    # GET request
    if request.method == 'GET':
        if id is not None:
            join_ProMetalbom_data = ProMetalbom.objects.filter(pro_metal_id=id)
            if not join_ProMetalbom_data:
                return Response(status=status.HTTP_404_NOT_FOUND)
            serializer = JoinedProMetalBomSerializer(
                join_ProMetalbom_data, many=True)
            return Response(serializer.data)
        else:
            join_ProMetalbom_data = ProMetalbom.objects.all()
            serializer = JoinedProMetalBomSerializer(
                join_ProMetalbom_data, many=True)
            return Response(serializer.data)

# ------------------------------------------------
# joinbomlist
# * INFO seach JoinedBomlistSerializer ที่ join ไว้แล้ว


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def handleData_Join_Bomlist(request, id=None):
    # GET request
    if request.method == 'GET':
        if id is not None:
            join_bomlist_data = ProBom.objects.filter(pro_sub_id=id)
            if not join_bomlist_data:
                return Response(status=status.HTTP_404_NOT_FOUND)
            serializer = JoinBomlist(join_bomlist_data, many=True)
            return Response(serializer.data)
        else:
            join_bomlist_data = ProBom.objects.all()
            serializer = JoinBomlist(join_bomlist_data, many=True)
            return Response(serializer.data)

# ----------------------------------------------------------
# ProCoat
# * INFO รายการชุบ


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def handleData_ProCoat(request, pro_code=None):
    # GET request
    if request.method == 'GET':
        print("call model name: ", pro_code)
        if pro_code is not None:
            ProCoat_data = ProCoat.objects.filter(pro_code=pro_code)
            if not ProCoat_data:
                return Response(status=status.HTTP_404_NOT_FOUND)
            serializer = ProCoatSerializer(ProCoat_data, many=True)
            return Response(serializer.data)
        else:
            ProCoat_data = ProCoat.objects.all()
            serializer = ProCoatSerializer(ProCoat_data, many=True)
            return Response(serializer.data)


# -------------------------------------------------------------------
# PlatType
# PlatTypeSerializer
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def handleData_PlatType(request, id=None):
    # GET request
    if request.method == 'GET':
        if id is not None:
            PlatType_data = PlatType.objects.filter(plat_type=id)
            if not PlatType_data:
                return Response(status=status.HTTP_404_NOT_FOUND)
            serializer = PlatTypeSerializer(PlatType_data, many=True)
            return Response(serializer.data)
        else:
            PlatType_data = PlatType.objects.all()
            serializer = PlatTypeSerializer(PlatType_data, many=True)
            return Response(serializer.data)


# ----------------------------------------------------------------------
# ProRingsizeSerializer
# ProRingsize
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def handleData_ProRingsize(request, id=None):
    # GET request
    if request.method == 'GET':
        if id is not None:
            ProRingsize_data = ProRingsize.objects.filter(pro_code=id)
            if not ProRingsize_data:
                return Response(status=status.HTTP_404_NOT_FOUND)
            serializer = ProRingsizeSerializer(ProRingsize_data, many=True)
            return Response(serializer.data)
        else:
            ProRingsize_data = ProRingsize.objects.all()
            serializer = ProRingsizeSerializer(ProRingsize_data, many=True)
            return Response(serializer.data)


#-------------------------------------------------------------------------
#stonedesc
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def handleData_StType(request, id=None,id2=None):
    # GET request
    if request.method == 'GET':
        if id is not None:
            StTypedata = StType.objects.filter(st_type=id,st_st_gp=id2)
            if not StTypedata:
                return Response(status=status.HTTP_404_NOT_FOUND)
            serializer = StTypeSerializer(StTypedata, many=True)
            return Response(serializer.data)
        else:
            StTypedata = StType.objects.all()
            serializer = StTypeSerializer(StTypedata, many=True)
            return Response(serializer.data)


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def handleData_StFancy(request, id=None):
    # GET request
    if request.method == 'GET':
        if id is not None:
            StFancydata = StFancy.objects.filter(st_new=id)
            if not StFancydata:
                return Response(status=status.HTTP_404_NOT_FOUND)
            serializer = StFancySerializer(StFancydata, many=True)
            return Response(serializer.data)
        else:
            StFancydata = StFancy.objects.all()
            serializer = StFancySerializer(StFancydata, many=True)
            return Response(serializer.data)

#StFront
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def handleData_StFront(request, id=None):
    # GET request
    if request.method == 'GET':
        if id is not None:
            StFrontdata = StFront.objects.filter(st_front=id)
            if not StFrontdata:
                return Response(status=status.HTTP_404_NOT_FOUND)
            serializer = StFrontSerializer(StFrontdata, many=True)
            return Response(serializer.data)
        else:
            StFrontdata = StFront.objects.all()
            serializer = StFrontSerializer(StFrontdata, many=True)
            return Response(serializer.data)

# StShape
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def handleData_StShape(request, id=None):
    # GET request
    if request.method == 'GET':
        if id is not None:
            StShapedata = StShape.objects.filter(st_shape=id)
            if not StShapedata:
                return Response(status=status.HTTP_404_NOT_FOUND)
            serializer = StShapeSerializer(StShapedata, many=True)
            return Response(serializer.data)
        else:
            StShapedata = StShape.objects.all()
            serializer = StShapeSerializer(StShapedata, many=True)
            return Response(serializer.data)
        

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def handleData_Stbott(request, id=None):
    # GET request
    if request.method == 'GET':
        if id is not None:
            StBottdata = StBott.objects.filter(st_bott=id)
            if not StBottdata:
                return Response(status=status.HTTP_404_NOT_FOUND)
            serializer = StBottSerializer(StBottdata, many=True)
            return Response(serializer.data)
        else:
            StBottdata = StBott.objects.all()
            serializer = StBottSerializer(StBottdata, many=True)
            return Response(serializer.data)
        

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def handleData_StGrade(request, id=None,id2=None):
    # GET request
    if request.method == 'GET':
        if id is not None:
            StGradedata = StGrade.objects.filter(st_grade=id,st_st_gp=id2)
            if not StGradedata:
                return Response(status=status.HTTP_404_NOT_FOUND)
            serializer = StGradeSerializer(StGradedata, many=True)
            return Response(serializer.data)
        else:
            StGradedata = StGrade.objects.all()
            serializer = StGradeSerializer(StGradedata, many=True)
            return Response(serializer.data)


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def handleData_ProEna(request, id=None):
    # GET request
    if request.method == 'GET':
        if id is not None:
            ProEnadata = ProEna.objects.filter(pro_sub_id=id)
            if not ProEnadata:
                return Response(status=status.HTTP_404_NOT_FOUND)
            serializer = ProEnaSerializer(ProEnadata, many=True)
            return Response(serializer.data)
        else:
            ProEnadata = ProEna.objects.all()
            serializer = ProEnaSerializer(ProEnadata, many=True)
            return Response(serializer.data)


#Enamel
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def handleData_Enamel(request, id=None):
    # GET request
    if request.method == 'GET':
        if id is not None:
            Enameldata = Enamel.objects.filter(pantone=id)
            if not Enameldata:
                return Response(status=status.HTTP_404_NOT_FOUND)
            serializer = EnamelSerializer(Enameldata, many=True)
            return Response(serializer.data)
        else:
            Enameldata = Enamel.objects.all()
            serializer = EnamelSerializer(Enameldata, many=True)
            return Response(serializer.data)

#ProMetalbomSerializer


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def handleData_ProMetalbom(request, id=None):
    # GET request
    if request.method == 'GET':
        if id is not None:
            ProMetalbomdata = ProMetalbom.objects.filter(pro_metal_id=id)
            if not ProMetalbomdata:
                return Response(status=status.HTTP_404_NOT_FOUND)
            serializer = ProMetalbomSerializer(ProMetalbomdata, many=True)
            return Response(serializer.data)
        else:
            ProMetalbomdata = ProMetalbom.objects.all()
            serializer = ProMetalbomSerializer(ProMetalbomdata, many=True)
            return Response(serializer.data)



class ImageAPIView_subpict(APIView):
    def get(self, request, pk,prosub):
        try:
            image = Subpict.objects.get(pk=pk,pro_sub=prosub)
            image_data = image.img_data_bytea
            response = HttpResponse(
                content=image_data, content_type='image/jpeg')
            response['Content-Disposition'] = f'inline; filename="{image.pro_code}"'
            return response
        except Subpict.DoesNotExist:
            # Log the message
            print(f"Subpict {pk} not found")

            # Raise Http404 exception
            raise Http404(f"Subpict {pk} not found")
