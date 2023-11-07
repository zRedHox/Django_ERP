from django.urls import path, re_path
from . import views
from .views import ImageAPIView, ImageAPIView_gfsol, ImageAPIView_subpict


urlpatterns = [
    path('setting/', views.handleData),
    path('setting/<str:id>', views.handleData),

    path('gfmaster/', views.handleDataGfmaster),
    path('gfmaster/<str:id>', views.handleDataGfmaster),  # pro_code

    path('gfsemi/', views.handleDataGfSemi),
    path('gfsemi/<path:id>', views.handleDataGfSemi),  # pro_code

    path('gfstockcode/', views.handleDataGfStockcode),
    path('gfstockcode/<str:id>', views.handleDataGfStockcode),  # pro_code

    path('gfmainroute/', views.handleDataGfMainroute),
    path('gfmainroute/<str:id>', views.handleDataGfMainroute),  # pro_code

    path('protype/', views.handleDataProType),
    path('protype/<str:id>', views.handleDataProType),  # pro_code

    path('prometalbase/', views.handleData_Metalbase),
    path('prometalbase/<str:pro_code>/<str:id2>', views.handleData_Metalbase),  # pro_code + mt_metal

    path('mtmetal/', views.handleData_MtMetal),
    path('mtmetal/<str:id>', views.handleData_MtMetal),  # pro_code

    path('mtcolor/', views.handleData_MtColor),
    path('mtcolor/<str:id>', views.handleData_MtColor),  # pro_code

    path('wfcust/', views.handleData_Wfcust),
    path('wfcust/<str:id>', views.handleData_Wfcust),  # pro_code

    path('mtgroup/', views.handleData_MtGroup),
    path('mtgroup/<str:id>', views.handleData_MtGroup),  # pro_code

    path('gfstockgroup/', views.handleData_GfStockgroup),
    path('gfstockgroup/<str:id>', views.handleData_GfStockgroup),  # pro_code


    path('modelpic/', views.handleData_Modelpicbytea),
    path('modelpic/<str:id>', views.handleData_Modelpicbytea),

    path('api/images/<str:pk>/', ImageAPIView.as_view(), name='image_api'),
    path('api/images_gfsol/<str:pk>/',
         ImageAPIView_gfsol.as_view(), name='image_gfsol_api'),

    path('api/images_subpict/<str:pk>/<str:prosub>',
         ImageAPIView_subpict.as_view(), name='image_subpict_api'),

    path('prospec/', views.handleData_ProSpec),
    path('prospec/<str:id>', views.handleData_ProSpec),  # pro_code


    path('prosub/<id>', views.handleData_ProSub),  # pro_code   สี
    path('prosub/', views.handleData_ProSub),

    path('routeprosub/<str:id>/<route>', views.handleData_routeProSub),

    path('prometal/<id>/<mt_metal>', views.handleData_ProMetal),  # pro_code
    path('prometal/', views.handleData_ProMetal),

    path('prometalbom/<str:id>', views.handleData_ProMetalbom), #pro_metal_id

    path('proroutegroup/<id>', views.handleData_ProRouteGroup),  # pro_code
    path('proroutegroup/', views.handleData_ProRouteGroup),

    path('prosemi/<str:id>/<routegroup>', views.handleData_ProSemi),  # pro_code
    path('prosemi/', views.handleData_ProSemi),

    path('gfroutecode/<id>', views.handleData_GfRoutecode),
    path('gfroutecode/', views.handleData_GfRoutecode),


    # SemiRouteId
    path('semirouteid/<path:id>', views.handleData_SemiRouteId),
    path('semirouteid/', views.handleData_SemiRouteId),

    #semiroute
    path('semiroute/<str:id>', views.handleData_SemiRoute),
    path('semiroute/', views.handleData_SemiRoute),

    path('joinprosemi/', views.pro_semi_list),
    path('joinprosemi/<str:id>', views.handleData_Join_ProSemi),  # ใช้ pro_code

    path('joinprometalbom/', views.pro_metalbomb_list),
    path('joinprometalbom/<str:id>',
         views.handleData_Join_ProMetalBom),  # ใช้ pro_metal_id

    path('joinbomlist/<id>', views.handleData_Join_Bomlist),  # pro_sub_id

    path('procoat/<pro_code>', views.handleData_ProCoat),
    path('procoat/', views.handleData_ProCoat),

    path('plattype/<id>', views.handleData_PlatType),

    path('proringsize/<id>', views.handleData_ProRingsize),

    path('sttype/<str:id>/<str:id2>', views.handleData_StType),

    path('stfancy/<str:id>', views.handleData_StFancy),

    path('stshape/<str:id>', views.handleData_StShape),

    path('stfront/<str:id>', views.handleData_StFront),

    path('stbott/<str:id>', views.handleData_Stbott),

    path('proena/<str:id>', views.handleData_ProEna),

    path('enamel/<str:id>', views.handleData_Enamel),

    path('stgrade/<str:id>/<str:id2>', views.handleData_StGrade)
    # handleData_Modelpicbytea
    #
]
