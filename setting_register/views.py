# ===========================================================================
#  todo                             README
#  todo         ในไฟล์นี้จะเป็นการจัดการข้อมูลก่อนส่งไปแสดงผลที่ไฟล์ .html ต่างๆ
#  todo         ประกอบด้วย ชื่อฟังชั่นเช่น def master , ตัวแปรเรียก url
#  todo         สุดท้ายส่งออกไปแสดงผล return render(request, 'ชื่อไฟล์ html', {ตัวแปรกส่งออกไปแสดงผล html})
# ===========================================================================


from icecream import ic
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from .form import settingForm
from .models import Setting
from rest_framework import views, status
from rest_framework.response import Response
from .serializers import SettingSerializer
import requests
from django.http import JsonResponse
import json
import html
from django.http import HttpResponse
import datetime
import pytz
# import zxing
import urllib3
import locale
from decimal import Decimal
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

local_tz = pytz.timezone('Asia/Bangkok')
now = datetime.datetime.now(local_tz)
# Create your views here.


# ==========================================================================
#                              ใช้สำหรับดึงข้อมูลจาก api
#                                  แล้วส่งไปที่ html
#
#
#
# ==========================================================================
def master(request):
    # Make a GET request to the API endpoint
    api_url = 'http://172.17.20.13/database/setting/'
    response = requests.get(api_url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        settings = response.json()
        # return render(request, 'setting_register/setting/setting_display_list.html', {'settings': settings})
        return render(request, 'setting_register/mock1.html', {'settings': settings})
    else:
        # Handle the error
        return HttpResponse('Error retrieving settings')


def master2(request):
    return render(request, 'setting_register/test2.html')


def master3(request):
    return render(request, 'setting_register/test3.html')


def master4(request):
    return render(request, 'setting_register/test4.html')


def scan_barcode(request):
    if request.method == 'POST':
        print(request.FILES)
        # Get the uploaded image from the request
        uploaded_file = request.FILES['image']

        # Create a zxing barcode reader object
        reader = zxing.BarCodeReader()

        # Decode the barcode from the uploaded image
        barcode = reader.decode(uploaded_file)

        # Get the barcode data and return it as a response
        barcode_data = barcode.raw
        return HttpResponse(barcode_data)

    return render(request, 'setting_register/scan_barcode.html')


# ================================================
#
#
#         รับข้อมูลจาก search box ไปเรียก api
#
#
# ================================================
# 127.0.0.1:8000
# 172.17.20.13
# https://172.17.20.26/database/api/images/BL-48371L/
def search_item(request):
    item_name = request.GET.get('item_name')
    #172.17.20.27  
    #127.0.0.1:8000
    ip_api_url = '172.17.20.27'
    # pro_sub_id = request.GET.get('pro_sub_id')
    print(item_name)
    if item_name:
        gfmaster_api_url = f'http://172.17.20.27/database/gfmaster/{item_name}'
        # print(gfmaster_api_url)
        prospec_api_url = f'http://172.17.20.27/database/prospec/{item_name}'
        # เอามาทำ scrool list ข้อแนะนำการผลิตรวม
        gf_mainroute_api_url = f'http://172.17.20.27/database/gfmainroute/'
        # เอามาทำ table สี
        pro_sub_api_url = f'http://172.17.20.27/database/prosub/{item_name}'
        # เอามาทำ table

        pro_route_group_api_url = f'http://172.17.20.27/database/proroutegroup/{item_name}'
        prosemi_api_url = f'http://172.17.20.27/database/prosemi/{item_name}'
        join_prosemi_list_api_url = f'http://172.17.20.27/database/join_prosemi/{item_name}'
        pro_coat_api_url = f'http://172.17.20.27/database/procoat/{item_name}'
        plat_type_api_url = f'http://172.17.20.27/database/plattype/'

        # ----------------------------- END OF SECTION ------------------------------

        gfmaster_response = requests.get(gfmaster_api_url, verify=False)
        print(gfmaster_response)
        print("Current date and time: year - month - date ")

        print(now.strftime("%Y-%m-%d %H:%M:%S"))
        prospec_response = requests.get(prospec_api_url, verify=False)
        gf_mainroute_response = requests.get(
            gf_mainroute_api_url, verify=False)
        pro_sub_response = requests.get(pro_sub_api_url, verify=False)
        pro_route_group_response = requests.get(
            pro_route_group_api_url, verify=False)
        prosemi_response = requests.get(prosemi_api_url, verify=False)
        pro_coat_response = requests.get(pro_coat_api_url, verify=False)
        # join_bom_response = requests.get(join_bom_api_url, verify=False)

        if gfmaster_response.status_code == 200:
            object_data = gfmaster_response.json() if gfmaster_response else {}
            prospec_data = prospec_response.json() if prospec_response else {}
            gf_mainroute_data = gf_mainroute_response.json() if gf_mainroute_response else {}
            prosub_data = pro_sub_response.json() if pro_sub_response else {}
            pro_route_group_data = pro_route_group_response.json(
            ) if pro_route_group_response else {}
            prosemi_data = prosemi_response.json() if prosemi_response else {}
            pro_coat_data = pro_coat_response.json() if pro_coat_response else {}
            prometal_data = ''

            # * INFO sorting data
            gf_mainroute_data_sorted = sorted(
                gf_mainroute_data, key=lambda x: x['rt_main'])

            gfmaster_datatable = [
                {
                    'pro_code': object_data['pro_code'].strip() if object_data['pro_code'] is not None else '',
                    'pro_type': object_data['pro_type'].strip() if object_data['pro_type'] is not None else '',
                    'std_925_wt': object_data['std_925_wt'].strip() if object_data['std_925_wt'] is not None else '',
                    'mold_wt': object_data['mold_wt'].strip() if object_data['mold_wt'] is not None else '',
                    'mold_metal': object_data['mold_metal'].strip() if object_data['mold_metal'] is not None else '',
                    'search_tag1': object_data['search_tag1'].strip() if object_data['search_tag1'] is not None else '',
                    'search_tag2': object_data['search_tag2'].strip() if object_data['search_tag2'] is not None else '',
                    'search_tag3': object_data['search_tag3'].strip() if object_data['search_tag3'] is not None else '',
                    'remark': object_data['remark'].strip() if object_data['remark'] is not None else '',
                    'surface': object_data['surface'].strip() if object_data['surface'] is not None else '',
                    'hallmark': str(object_data['hallmark']).strip() if object_data['hallmark'] is not None else '',
                    'cus_id': str(object_data['cus']).strip() if object_data['cus'] is not None else '',
                    'route_check': object_data['route_check'].strip() if object_data['route_check'] is not None else '',
                    'route_checkdate': object_data['route_checkdate'].strip() if object_data['route_checkdate'] is not None else '',
                    'route_checkuser': object_data['route_checkuser'].strip() if object_data['route_checkuser'] is not None else '',
                    'pd_gd': object_data['pd_gd'].strip() if object_data['pd_gd'] is not None else '',
                    'route_remark': object_data['route_remark'].strip() if object_data['route_remark'] is not None else '',
                    'sale_remark': object_data['sale_remark'].strip() if object_data['sale_remark'] is not None else '',
                    'mold_type': object_data['mold_type'].strip() if object_data['mold_type'] is not None else '',
                    'mold_model': object_data['mold_model'].strip() if object_data['mold_model'] is not None else '',
                    'cast_925wt':object_data['cast_925wt'].strip() if object_data['cast_925wt'] is not None else "0.00",
                    'yg_wt': object_data['yg_wt'].strip() if object_data['yg_wt'] is not None else "0.00",
                    'cus_yg_wt':object_data['cus_yg_wt'].strip() if object_data['cus_yg_wt'] is not None else "0.00",
                    'yg_castwt':object_data['yg_castwt'].strip() if object_data['yg_castwt'] is not None else "0.00",
                    'wg_wt':object_data['wg_wt'].strip() if object_data['wg_wt'] is not None else "0.00",
                    'cus_wg_wt': object_data['cus_wg_wt'].strip() if object_data['cus_wg_wt'] is not None else "0.00",
                    'wg_castwt': object_data['wg_castwt'].strip() if object_data['wg_castwt'] is not None else "0.00",
                    'pt_wt': object_data['pt_wt'].strip() if object_data['pt_wt'] is not None else "0.00",
                    'cus_pt_wt': object_data['cus_pt_wt'].strip() if object_data['cus_pt_wt'] is not None else "0.00",
                    'si_wt': object_data['si_wt'].strip() if object_data['si_wt'] is not None else "0.00",
                    'cus_si_wt': object_data['cus_si_wt'].strip() if object_data['cus_si_wt'] is not None else "0.00",
                    'true_wt': object_data['true_wt'].strip() if object_data['true_wt'] is not None else "0.00",
                    'sil_chain': object_data['sil_chain'].strip() if object_data['sil_chain'] is not None else "0.00",
                    'ag_wt': object_data['ag_wt'].strip() if object_data['ag_wt'] is not None else "0.00",
                    'no_cast': object_data['no_cast'].strip() if object_data['no_cast'] is not None else None,

                }]

            # ส่งเลข pro_type จาก gf_master ไปหา desc_th ใน pro_type   บอก กำไล , สร้อย
            pro_type = object_data['pro_type']
            pro_type_api_url = f'http://172.17.20.27/database/protype/{pro_type}'
            pro_type_response = requests.get(pro_type_api_url, verify=False)
            pro_type_data = pro_type_response.json() if pro_type_response else {}
            pro_type_desc = pro_type_data['desc_th']

            mainroute_datatable = []
            for item in gf_mainroute_data_sorted:
                mainroute_datatable.append({
                    'rt_main': item['rt_main'].strip() if item['rt_main'] is not None else '',
                    'rt_desc': item['rt_desc'].strip() if item['rt_desc'] is not None else ''
                })

            prospec_datatable = []
            for item in prospec_data:
                prospec_datatable.append({
                    'prospec_procode': item['pro_code'].strip() if item['pro_code'] is not None else '',
                    'pd_spec': item['pd_spec'].strip() if item['pd_spec'] is not None else '',
                    'prospec_rt_main': item['rt_main'].strip()if item['rt_main'] is not None else '',
                })

            # Convert to JSON
            prospec_datatable_json = json.dumps(prospec_datatable)

            temp_rt_main = {'prospec_rt_main': []}
            for item in prospec_data:
                temp_rt_main['prospec_rt_main'].append(item['rt_main'].strip())

            # เอาค่าจากฟีล rt_main ใน prospec_data
            value_temp = {item['rt_main'].strip() for item in prospec_data}

            prosub_datatable = []
            list_of_prometal_id = []
            prometalbom_data_list = []
            for item in prosub_data:
                pro_code = item['pro_code'].strip() 
                mt_metal = item['mt_metal'].strip() 
                prometal_api_url = f'http://{ip_api_url}/database/prometal/{item_name}/{mt_metal}'
                prometal_response = requests.get(
                    prometal_api_url, verify=False)
                prometal_data = prometal_response.json() if prometal_response else {}
                #print(prometal_data)
                true_wt = [d['true_wt'] for d in prometal_data]
                std_conv_wt = [d['std_conv_wt'] for d in prometal_data]
                wax_wt = [d['wax_wt'] for d in prometal_data]
                fin_wt = [d['fin_wt'] for d in prometal_data]
                # print(mt_metal)
                # print(prometal_data)
                # plat_type_desc = plat_type_desc_list[0] if plat_type_desc_list else None
                # procoat_remark = item['remark']
                # prosub_datatable.append({
                #     'pro_sub_id': str(item['pro_sub_id']).strip(),
                #     'color': item['pro_sub'].strip(),
                #     'desc': item['description'].strip(),
                #     'metal': item['mt_metal'].strip(),
                # })
                prometalbase_url = f'http://172.17.20.27/database/prometalbase/{item_name}/{mt_metal}'
                prometalbase_response = requests.get(
                    prometalbase_url, verify=False)
                prometalbase_data = prometalbase_response.json() if prometalbase_response else {}
 
                #for item in prometalbase_data:
                if prometalbase_data:
                    prometal_id = prometalbase_data['pro_metal_id']
                    list_of_prometal_id.append({
                        'pro_metal_id': prometal_id
                    })
                   

                prosub_datatable.append({
                    'pro_sub_id': str(item['pro_sub_id']).strip() ,
                    'pro_code':pro_code ,
                    'pro_sub':item['pro_sub'].rstrip(),
                    'pro_metal_id': prometalbase_data.get('pro_metal_id', ''),
                    'color': item['pro_sub'].strip()  ,
                    'desc': item['description'].strip()if item['description'] is not None else '',
                    'metal': item['mt_metal'].strip()if item['mt_metal'] is not None else '',
                })
     
            #* หา acs 
            i = 1
            for item in list_of_prometal_id:
                pro_metal_id = item['pro_metal_id']
                prometalbom_url = f'http://172.17.20.27/database/prometalbom/{pro_metal_id}'
                prometalbom_response = requests.get(prometalbom_url,verify=False)
                prometalbom_data = prometalbom_response.json() if prometalbom_response else {}
                
 
                for item in prometalbom_data:
                    stock_id = item['stock_id']
                    stockcode_url = f'http://172.17.20.27/database/gfstockcode/{stock_id}'
                    stockcode_response = requests.get(
                        stockcode_url, verify=False)
                    stockcode_data = stockcode_response.json() if stockcode_response else {}
              
                    prometalbom_data_list.append({
                            'pro_metal_id': str(pro_metal_id),
                            'stock_id':item['stock_id'].rstrip() if item['stock_id'] is not None else '',
                            'seq': i ,
                            'stockcode': stockcode_data['stockcode'].rstrip() if stockcode_data['stockcode'] is not None else '',
                            'stockdesc': stockcode_data['stockdesc'].rstrip() if stockcode_data['stockdesc'] is not None else '',
                            'qty':item['qty'].rstrip() if item['qty'] is not None else '',
                            'unit_qty':stockcode_data['unit_qty'].rstrip()  if stockcode_data['unit_qty'] is not None else '',
                            'cus_com': ''
                        })
                    i = i + 1
            #* ได้ acs list แล้ว 
            prometalbom_data_list_json = json.dumps(prometalbom_data_list)

            unique_pro_metal_ids = set()
            unique_prometalbom_data_list = []

            for item in prometalbom_data_list:
                pro_metal_id = item['pro_metal_id']
                if pro_metal_id not in unique_pro_metal_ids:
                    unique_pro_metal_ids.add(pro_metal_id)
                    unique_prometalbom_data_list.append(item)
            unique_prometalbom_data_list_json = json.dumps(
                unique_prometalbom_data_list)



            # * bomlist
            bomlist = []
            # * 'งานลงสี'
            colorlist = []
            # * supply
            supply_list = []
            setting_numeric_part = ''
            for item in prosub_datatable:
                pro_sub_id = item['pro_sub_id'].strip()
                join_bom_api_url = f'http://172.17.20.27/database/joinbomlist/{pro_sub_id}'
                join_bom_response = requests.get(
                    join_bom_api_url, verify=False)
                join_bom_data = join_bom_response.json() if join_bom_response else {}

                proena_api_url = f'http://172.17.20.27/database/proena/{pro_sub_id}'
                proena_response = requests.get(proena_api_url, verify=False)
                proena_data = proena_response.json() if proena_response else {}
                for item in proena_data:
                    pantone_code = item['pantone'].rstrip()
                    pn_no = item['pn_no']
                    enamel_api_url = f'http://172.17.20.27/database/enamel/{pantone_code}'
                    enamel_response = requests.get(
                        enamel_api_url, verify=False)
                    enamel_data = enamel_response.json() if enamel_response else {}
                    for item in enamel_data:
                        color = item['description'].rstrip() if item['description'] is not None else ''
                        colorlist.append({
                            'pro_sub_id':pro_sub_id,
                            'pn_no': pn_no,
                            'color_code': pantone_code,
                            'color_desc': color
                        })
                

                for item in join_bom_data:
                    if item['stockgroup'] == '03':
                        setting = item['setting']
                        setting_numeric_part = setting.split(
                            '(')[-1].strip(') ')
                        # print(setting_numeric_part)
                        setting_url = f'http://172.17.20.27/database/setting/{setting_numeric_part}'
                        setting_url_response = requests.get(
                            setting_url, verify=False)
                        setting_data = setting_url_response.json() if setting_url_response else {}
                        

                        bomlist.append({
                            'pro_sub_id': pro_sub_id,
                            'seq': item['seq'].strip() if item['seq'] is not None else '',
                            'stockcode': item['stockcode'].strip() if item['stockcode'] is not None else '',
                            'stockdesc': item['stockdesc'].strip() if item['stockdesc'] is not None else '',
                            'qty': item['qty'].strip() if item['qty'] is not None else '',
                            'unit_qty': item['unit_qty'].strip() if item['unit_qty'] is not None else '',
                            'setting': setting_data['description'].strip(),
                            'wax_fg': item['wax_fg'].strip() if item['wax_fg'] is not None else '',
                            'cus_com': item['cus_com'].strip() if item['cus_com'] is not None else '',
                        })
                    if item['stockgroup'] == '05':
                        supply_list.append({
                            'pro_sub_id': pro_sub_id,
                            'seq': item['seq'].strip() if item['seq'] is not None else '',
                            'stockcode': item['stockcode'].strip() if item['stockcode'] is not None else '',
                            'stockdesc': item['stockdesc'].strip() if item['stockdesc'] is not None else '',
                            'qty': item['qty'].strip() if item['qty'] is not None else '',
                            'unit_qty': item['unit_qty'].strip() if item['unit_qty'] is not None else '',
                            'cus_com': item['cus_com'].strip() if item['cus_com'] is not None else '',
                        })

                  

            #print(unique_prometalbom_data_list)
            #print(bomlist)
            bomlist_json = json.dumps(bomlist)
            colorlist_json = json.dumps(colorlist)
            #print(bomlist_json)
            sorted_color_list = sorted(colorlist, key=lambda x: x["pn_no"])
            sorted_supply_list = sorted(supply_list, key=lambda x: x["seq"])
            sorted_color_list_json = json.dumps(sorted_color_list)
            sorted_supply_list_json = json.dumps(sorted_supply_list)
            #print(sorted_supply_list_json)
       

            #! stonedesc
            stone_desc_extracted = []
            json_stone_code = []
            stone_data_json = {}
            for item in bomlist:
                stone_desc_extracted.append(item['stockcode'].strip())
                # json_stone_code.append({
                #     'stonecode':item['stockcode'].strip() if item['stockcode'] is not None else ''
                # })
            # print(stone_desc_extracted)
            # print(json_stone_code)

            for _stcode in stone_desc_extracted:
                _stgp = _stcode[0:1]
                _sttype = _stcode[1:3]
                _front = _stcode[3:5]
                _bott = _stcode[5:7]
                _shape = _stcode[7:9]
                _fancy = _stcode[3:18]
                _width = _stcode[9:12]
                _lenght = _stcode[12:15]
                _height = _stcode[15:18]
                _grade = _stcode[18:19]

                stonedesc_url = f'http://172.17.20.27/database/sttype/{_sttype}/{_stgp}'
                stonedesc_response = requests.get(stonedesc_url, verify=False)
                stonedesc_data = stonedesc_response.json() if stonedesc_response else {}
                for item in stonedesc_data:
                    _xsttype_st_fix = item['st_fix'] if item['st_fix'] is not None else ''
                    _xsttype_st_desc = item['st_desc'] if item['st_desc'] is not None else ''
                # print(stonedesc_data)
                    if (_front == 'FC') or (_front == 'FF') or (_height > '999'):
                        # Fancy
                        fancy_url = f'http://172.17.20.27/database/stfancy/{_fancy}'
                        fancy_response = requests.get(fancy_url, verify=False)
                        fancy_data = fancy_response.json() if fancy_response else {}
                        # print(fancy_data)
                        for item in fancy_data:
                            _st_shape = item['st_shape']
                            _st_front = item['st_front']
                            _st_bott = item['st_bott']
                            _st_width = item['st_width']

                            _st_long = item['st_long']
                            _st_h_font = item['st_h_font']
                            _st_h_bott = item['st_h_bott']
                            _st_h_line = item['st_h_line']

                            _st_h_cross = item['st_h_cross']
                            _st_remark = item['st_remark']

                            if _st_shape:

                                stshape_url = f'http://172.17.20.27/database/stshape/{_st_shape}'
                                stshape_response = requests.get(
                                    stshape_url, verify=False)
                                stshape_data = stshape_response.json() if stshape_response else {}
                                for item in stshape_data:
                                    _sh = ' , ' + \
                                        item['st_desc'].rstrip(
                                        ) if item['st_desc'] is not None else ''
                            if _st_front:
                                stfront_url = f'http://172.17.20.27/database/stfront/{_st_front}'
                                stfront_response = requests.get(
                                    stfront_url, verify=False)
                                stfront_data = stfront_response.json() if stfront_response else {}
                                for item in stfront_data:
                                    _fn = ' , ' + \
                                        item['st_desc'].rstrip(
                                        ) if item['st_desc'] is not None else ''
                            if _st_bott:
                                stbott_url = f'http://172.17.20.27/database/stbott/{_st_bott}'
                                stbott_response = requests.get(
                                    stbott_url, verify=False)
                                stbott_data = stbott_response.json() if stbott_response else {}
                                for item in stbott_data:
                                    _bt = ' , ' + \
                                        item['st_desc'].rstrip(
                                        ) if item['st_desc'] is not None else ''
                            if _st_width != '0.00':
                                _wd = ' กว้าง: ' + str(_st_width)
                            else:
                                _wd = ''
                            if _st_long != '0.00':
                                _ln = ' ยาว: ' + str(_st_long)
                            else:
                                _ln = ''
                            if _st_h_font != '0.00':
                                _hf = ' สูงหน้า: ' + str(_st_h_font)
                            else:
                                _hf = ''
                            if _st_h_bott != '0.00':
                                _hb = ' สูงก้น: ' + str(_st_h_bott)
                            else:
                                _hb = ''
                            if _st_h_line != '0.00':
                                _hl = ' สูงขอบ: ' + str(_st_h_line)
                            else:
                                _hl = ''
                            if _st_h_cross != '0.00':
                                _cl = ' ทะแยงมุม: ' + str(_st_h_cross)
                            else:
                                _cl = ''
                            if _st_remark:
                                _rm = ' หมายเหตุ: ' + _st_remark.rstrip()
                            else:
                                _rm = ''
                            if _xsttype_st_fix == 'Y':
                                _bb = 'ไม่มีเกรด'
                            else:
                                _xgrade_url = f'http://172.17.20.27/database/stgrade/{_grade}/{_stgp}'
                                _xgrade_response = requests.get(
                                    _xgrade_url, verify=False)
                                _xgrade_data = _xgrade_response.json() if _xgrade_response else {}
                                for item in _xgrade_data:
                                    _bb = item['st_desc'].rstrip(
                                    ) if item['st_desc'] is not None else ''

                            _dd = _xsttype_st_desc.rstrip() + ','+_sh + _fn+_bt+',ขนาด '+_wd+_ln + \
                                _hf+' ' + _hb+' '+_hl+' '+_cl+','+_bb+_rm
                            # print(_dd)
                            json_stone_code.append({
                                'stockcode': _stcode,
                                'desc': _dd if _dd is not None else ''
                            })

                            # print(json_stone_code)

                    else:
                        stfront_url = f'http://172.17.20.27/database/stfront/{_front}'
                        stfront_response = requests.get(
                            stfront_url, verify=False)
                        stfront_data = stfront_response.json() if stfront_response else {}
                        for item in stfront_data:
                            st_fnt_desc = item['st_desc'] if item['st_desc'] is not None else ''

                        stbott_url = f'http://172.17.20.27/database/stbott/{_bott}'
                        stbott_response = requests.get(
                            stbott_url, verify=False)
                        stbott_data = stbott_response.json() if stbott_response else {}
                        for item in stbott_data:
                            st_bott_desc = item['st_desc'] if item['st_desc'] is not None else ''

                        stshape_url = f'http://172.17.20.27/database/stshape/{_shape}'
                        stshape_response = requests.get(
                            stshape_url, verify=False)
                        stshape_data = stshape_response.json() if stshape_response else {}
                        for item in stshape_data:
                            st_shape_desc = item['st_desc'] if item['st_desc'] is not None else ''
                            st_short = item['st_short'] if item['st_short'] is not None else ''

                        if (_shape != 'RD') and (_shape != 'RM') and (_shape != 'SQ'):
                            # กว้าง
                            if _width[0:1] == '0':
                                _aa = _width[1:2]+'.'+_width[2:3]
                            else:
                                _aa = _width[0:2]+'.'+_width[2:3]

                            #   ยาว
                            if _lenght[0:1] == '0':
                                _aa = _aa+'X' + _lenght[1:2]+'.'+_lenght[2:3]
                            else:
                                _aa = _aa+'X'+_lenght[0:2]+'.'+_lenght[2:3]

                            # สูง
                            if (_height <= '999'):
                                _hx = locale.atof(_height)
                                if (_hx >= 0.0) and (_height != '999'):
                                    if _height[0:1] == '0':
                                        _aa = _aa+'X' + \
                                            _height[1:2]+'.'+_height[2:3]
                                    else:
                                        _aa = _aa+'X' + \
                                            _height[0:2]+'.'+_height[2:3]

                        else:
                            # กว้าง # Sieve size ไซด์ร่อน
                            if _width[0:1] == '0':
                                _aa = _width[1:2]+'.'+_width[2:3]
                            else:
                                _aa = _width[0:2]+'.'+_width[2:3]

                        if _xsttype_st_fix == 'Y':
                            _bb = 'ไม่มีเกรด'
                        else:
                            _xgrade_url = f'http://172.17.20.27/database/stgrade/{_grade}/{_stgp}'
                            _xgrade_response = requests.get(
                                _xgrade_url, verify=False)
                            _xgrade_data = _xgrade_response.json() if _xgrade_response else {}
                            for item in _xgrade_data:
                                _bb = item['st_desc'] if item['st_desc'] is not None else ''

                        _jea = _front+_bott

                        if _shape != 'RD':
                            if (_jea != 'DIDI') and (_jea != 'DIST') and (_jea != 'DISD') and (_jea != 'SDSD'):
                                _dd = _xsttype_st_desc.rstrip() + ', ' + st_fnt_desc.rstrip() + ', ' + \
                                    st_bott_desc.rstrip()+', '+st_shape_desc.rstrip()+',ขนาด '+_aa+' mm.'+_bb
                            else:
                                _dd = _xsttype_st_desc.rstrip()+', ' + st_short.rstrip() + \
                                    ',ขนาด '+_aa+' mm.'+_bb
                        else:
                            # Sieve size ไซด์ร่อน
                            if (_jea != 'DIDI') and (_jea != 'DIST') and (_jea != 'DISD') and (_jea != 'SDSD'):
                                _dd = _xsttype_st_desc.rstrip() + ', ' + st_fnt_desc.rstrip() + ', ' + \
                                    st_bott_desc.rstrip()+', '+st_shape_desc.rstrip()+',ขนาด '+_aa+' '+_bb
                            else:
                                _dd = _xsttype_st_desc.rstrip()+', ' + st_short.rstrip()+',ขนาด '+_aa+' '+_bb

                # print(_dd)
                json_stone_code.append({
                    'stockcode': _stcode if _stcode is not None else '',
                    'desc': _dd if _dd is not None else ''
                })
                if json_stone_code:
                    stone_data_json = json.dumps(
                        json_stone_code, ensure_ascii=False)
                    # print(stone_data_json)

            prometal_datatable = []
            prometal_metallist = []
            for item in prometal_data:
                prometal_datatable.append({
                    'mt_metal': item['mt_metal'].strip() if item['mt_metal'] is not None else '',
                    'sub_metal':item['sub_metal'].strip() if item['sub_metal'] is not None else '',
                    'mt_mast': item['mt_mast'].strip() if item['mt_mast'] is not None else '', #โลหะหลัก
                    'mt_cast': item['mt_cast'].strip()if item['mt_cast'] is not None else '', #งานหล่อเบิก
                    'stn_set':item['stn_set'].strip()if item['stn_set'] is not None else '',#ฝังพลอย
                    'true_wt': item['true_wt'].strip() if item['true_wt'] is not None else '',
                    'std_wt': item['std_conv_wt'].strip() if item['std_conv_wt'] is not None else '',
                    'cus_wt':item['cus_wt'].strip() if item['cus_wt'] is not None else '',
                    'wax_wt': item['wax_wt'].strip() if item['wax_wt'] is not None else '',
                    'cast_wt':item['cast_wt'].strip() if item['cast_wt'] is not None else '',
                    'fin_wt': item['fin_wt'].strip() if item['fin_wt'] is not None else '',
                })
                prometal_metallist.append({
                    'mt_metal': item['mt_metal'].strip() if item['mt_metal'] is not None else '',
                })

            unique_pro_metal_name = set()
            unique_prometal_list = []

            for item in prometal_metallist:
                pro_metal_name = item['mt_metal']
                if pro_metal_name not in unique_pro_metal_name:
                    unique_pro_metal_name.add(pro_metal_name)
                    unique_prometal_list.append(item)
            # print(unique_prometalbom_data_list)
            unique_prometal_list_json = json.dumps(
                unique_prometal_list)
            print(unique_prometal_list_json)
            prometal_datatable_json = json.dumps(prometal_datatable)

            pro_route_group_datatable = []
            for item in pro_route_group_data:
                pro_route_group_datatable.append({
                    'pro_routegroup': item['routegroup'].strip() if item['routegroup'] is not None else '',
                })

            prosemi_datatable = []
            for item in prosemi_data:
                prosemi_datatable.append({
                    'semi': item['semi_code'].strip() if item['semi_code'] is not None else '',
                    'desc': item['cast_metal'].strip() if item['cast_metal'] is not None else '',
                    'job': item['semi_char'].strip() if item['semi_char'] is not None else '',
                })

            # pro_coat_data
            table_procoat = []
            for item in pro_coat_data:
                pro_code = item['pro_code'].strip()
                plat_type = item['plat_type']
                plat_type_api_url = f'http://172.17.20.27/database/plattype/{plat_type}'
                plat_type_response = requests.get(
                    plat_type_api_url, verify=False)
                plat_type_data = plat_type_response.json() if plat_type_response else {}
                plat_type_desc_list = [d['description']
                                       for d in plat_type_data]
                plat_type_desc = plat_type_desc_list[0] if plat_type_desc_list else None
                procoat_remark = item['remark']
                table_procoat.append({
                    'pro_code': pro_code,
                    'plat_type': plat_type,
                    'plat_type_desc': plat_type_desc,   # บอก ที่ผิวตัวเรือนด้านนอกและวงในกำไล
                    'procoat_remark': procoat_remark,
                })

            table_procoat_json = json.dumps(table_procoat, ensure_ascii=False)

            # * proringsize
            pro_ringsize_table = []
            pro_ringsize_api_url = f'http://172.17.20.27/database/proringsize/{item_name}'
            pro_ringsize_response = requests.get(
                pro_ringsize_api_url, verify=False)
            proringsize_data = pro_ringsize_response.json() if pro_ringsize_response else {}
            for item in proringsize_data:
                pro_ringsize_table.append({
                    'ringsize': item['ringsize'].strip()
                })

            pro_route_group_response = requests.get(
                pro_route_group_api_url, verify=False)
            pro_route_data = pro_route_group_response.json() if pro_route_group_response else {}
            routegroup_list = []
            for item in pro_route_data:
                routegroup_list.append({
                    'pro_code':item['pro_code'],
                    'routegroup':item['routegroup'].strip()
                })
            #routegroup_value = pro_route_data[0]['routegroup']
            #ic(pro_route_data)
            #ic(routegroup_list)

            semi_code_list = []
            routeProsub_list = []
            for item in routegroup_list:
                routegroup = item['routegroup']

                routeProsub_api_url = f'http://172.17.20.27/database/routeprosub/{item_name}/{routegroup}'
                routeProsub_response = requests.get(routeProsub_api_url,verify=False)
                routeProsub_data = routeProsub_response.json() if routeProsub_response else {}
                for item in routeProsub_data:
                    routeProsub_list.append({
                        'pro_code':item['pro_code'].strip(),
                        'pro_sub':item['pro_sub'].strip(),
                        'routegroup':item['routegroup'].strip(),
                        'mt_metal':item['mt_metal'].strip(),
                        'description':item['description'].strip()
                    })

                pro_semi_api_url = f'http://172.17.20.27/database/prosemi/{item_name}/{routegroup}' ##รอเปลี่ยนpath กลับเป็น 172.17.20.27
                pro_semi_response = requests.get(
                    pro_semi_api_url, verify=False)
                pro_semi_data = pro_semi_response.json() if pro_semi_response else {}
                
                for item in pro_semi_data:
                    semi_code_list.append({
                        'pro_code':item['pro_code'],
                        'routegroup':item['routegroup'],
                        'semi_code': item['semi_code'].strip() if item['semi_code'] is not None else '',
                        'semi_char':item['semi_char'].strip() if item['semi_char'] is not None else '',
                        'cast_metal':item['cast_metal'].strip() if item['cast_metal'] is not None else '',
                    })
    
            #ic(routeProsub_list)
            #ic(semi_code_list)
            

            semi_route_id_list = []
            for item in semi_code_list:
                semi_code = item['semi_code']
                # รอเปลี่ยน path
                gf_semi_api_url = f'http://172.17.20.27/database/gfsemi/{semi_code}'
                gf_semi_response = requests.get(gf_semi_api_url,verify=False)
                gf_semi_data = gf_semi_response.json() if gf_semi_response else {}
                #ic(gf_semi_data)

                semi_route_id_api_url = f'http://172.17.20.27/database/semirouteid/{semi_code}'
                semi_route_id_response = requests.get(semi_route_id_api_url,verify=False)
                semi_route_id_data = semi_route_id_response.json() if semi_route_id_response else {}
            
                for item in semi_route_id_data:
                    active = item['active'].strip()
                    if active == 'Y':
                        semi_route_id_list.append({
                            'semi_code':item['semi_code'].strip(),
                            'semi_route_id':item['semi_route_id'],
                            'comp':item['complete']
                        })
                      
                

            for item in semi_code_list:
                for route_item in semi_route_id_list:
                    if item['semi_code'] == route_item['semi_code']:
                        item['comp'] = route_item['comp']
            



            semi_route_list = []
            final_route_list = []
            semi_route_data_list= []
            for item in semi_route_id_list:
                semi_route_id = item['semi_route_id']
                semi_route_api_url = f'http://172.17.20.27/database/semiroute/{semi_route_id}'
                semi_route_response = requests.get(semi_route_api_url,verify=False)
                semi_route_data = semi_route_response.json() if semi_route_response else {}
                # Append data to the list
                semi_route_data_list.extend(semi_route_data)
            #ic(semi_route_data_list)

            gf_routecode_data_list = []
            for item in semi_route_data_list:
                routecode = item['routecode_id']
                gf_routecode_api_url = f'http://172.17.20.27/database/gfroutecode/{routecode}'
                gf_routecode_response = requests.get(gf_routecode_api_url,verify=False)
                gf_routecode_data = gf_routecode_response.json() if gf_routecode_response else {}
                gf_routecode_data_list.extend(gf_routecode_data)
    
            #ic(gf_routecode_data_list)
                   
            for semi_route_data, gf_routecode_data in zip(semi_route_data_list,gf_routecode_data_list):
                semi_route_id = semi_route_data['semi_route_id']
                route_seq = semi_route_data['route_seq']
                rt_code = gf_routecode_data['rt_code']
                rt_desc = gf_routecode_data['rt_desc']
                rt_unit = gf_routecode_data['rt_unit']
                loop = semi_route_data['rt_loop']
                qty = float(semi_route_data['qty'])
                qty_str = str(semi_route_data['qty'])
                stdtime = int(semi_route_data['u_stdtime_sec'])*qty
                std_min = int(stdtime)//60
                std_sec = int(stdtime)%60
                if std_min == 0 and std_sec > 0 :
                    stdtime_formateed = f'0m {std_sec}s'
                if std_min > 0 and std_sec == 0:
                    stdtime_formateed = f'{std_min}m'
                if std_min == 0 and std_sec ==0:
                    stdtime_formateed = f'0m'
                else:
                    stdtime_formateed = f'{std_min}m {std_sec}s'
                realtime = int(semi_route_data['p_realtime_sec'])
                realtime_min = realtime//60
                realtime_sec = realtime%60
                if realtime_min == 0 and realtime_sec > 0:
                    realtime_formatted = f'0m {realtime_sec}s'
                if realtime_min > 0 and realtime_sec == 0:
                    realtime_formatted = f'{realtime_min}m'
                if realtime_min == 0 and realtime_sec == 0:
                    realtime_formatted = f'0m'
                else:
                    realtime_formatted = f'{realtime_min}m {realtime_sec}s'
                

                final_route_list.append({
                        'semi_route_id':semi_route_id,
                        'route_seq':route_seq,
                        'rt_code':rt_code,
                        'rt_desc':rt_desc.strip(),
                        'loop':loop,
                        'rt_unit': rt_unit,
                        'qty': qty,
                        'stdtime': stdtime_formateed,
                        'realtime': realtime_formatted,

                    })
                        

            ic(final_route_list)
            routeProsub_list_json = json.dumps(routeProsub_list,ensure_ascii=False)
            semi_code_list_json = json.dumps(semi_code_list,ensure_ascii=False)
            semi_route_id_list_json = json.dumps(semi_route_id_list,ensure_ascii=False)
            routegroup_list_json = json.dumps(routegroup_list,ensure_ascii=False)
            route_list_json = json.dumps(final_route_list, ensure_ascii=False)


            context = {'item_name': item_name, 'pro_code': object_data['pro_code'], 'pro_type': object_data['pro_type'], 'std_925_wt': object_data['std_925_wt'], 'mold_wt': object_data['mold_wt'], 'mold_metal': object_data['mold_metal'], 'search_tag1': object_data['search_tag1'],
                       'search_tag2': object_data['search_tag2'], 'search_tag3': object_data['search_tag3'], 'remark': object_data['remark'], 'surface': object_data['surface'], 'hallmark': str(object_data['hallmark']), 'cus_id': str(object_data['cus']), 'route_check': object_data['route_check'],
                       'route_checkdate': object_data['route_checkdate'], 'route_checkuser': object_data['route_checkuser'], 'pd_gd': object_data['pd_gd'], 'route_remark': object_data['route_remark'], 'sale_remark': object_data['sale_remark'], 'mold_type': object_data['mold_type'], 'mold_model': object_data['mold_model'],
                       'prospec_datatable': prospec_datatable, 'mainroute_datatable': mainroute_datatable, 'value_temp': value_temp, 'prospec_datatable_json': prospec_datatable_json, 'prosub_datatable': prosub_datatable, 'prometal_datatable': prometal_datatable, 'gfmaster_datatable': gfmaster_datatable, 'pro_route_group_datatable': pro_route_group_datatable, 'prosemi_datatable': prosemi_datatable,
                       'table_procoat': table_procoat, 'pro_type_desc': pro_type_desc, 'table_procoat_json': table_procoat_json, 'pro_ringsize_table': pro_ringsize_table, 'bomlist': bomlist, 'bomlist_json': bomlist_json, 'stone_data_json': stone_data_json, 'colorlist': sorted_color_list_json, 'supply_list': sorted_supply_list_json, 'pro_metal_id': list_of_prometal_id, 'prometalbom_data': unique_prometalbom_data_list_json,\
                       'unique_prometal_list': unique_prometal_list, 'prometal_datatable_json': prometal_datatable_json,'routegroup_list':routegroup_list,'routegroup_list_json':routegroup_list_json,'routeProsub_list_json':routeProsub_list_json, 'routeProsub_list':routeProsub_list,'semi_code_list':semi_code_list, 'route_list': final_route_list, 'route_list_json': route_list_json, \
                       'semi_code_list_json': semi_code_list_json, 'semi_route_id_list_json': semi_route_id_list_json}

            return render(request, 'setting_register/test3.html', context)

        # If the response is not successful, display an error message
        elif gfmaster_response.status_code == 404:
            return HttpResponse('ไม่มีเบอร์โมเดลนี้')
        else:
            error_message = f"Error: {gfmaster_response.status_code} - {gfmaster_response.reason}"
            context = {'error_message': error_message}
            return render(request, 'setting_register/test3.html', context)
    else:
        return render(request, 'setting_register/test3.html')
# ============================= END OF SECTION ==============================


def index(request):
    # Retrieve the bank holidays data from the API
    # Render the data in a template or return a JSON response
    return render(request, 'setting_register/index.html')

# ===========================================================================
#  !                           ตั้งแต่ข้างล่างเป็นต้นไปยังไม่ได้ใช้
# ===========================================================================


def setting_display_list(request):
    # Make a GET request to the API endpoint
    api_url = 'http://172.17.20.13/database/setting/'
    response = requests.get(api_url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        settings = response.json()
        return render(request, 'setting_register/setting/setting_display_list.html', {'settings': settings})
    else:
        # Handle the error
        return HttpResponse('Error retrieving settings')


def setting_create(request):
    if request.method == 'POST':
        api_url = 'http://172.17.20.13/database/setting/'
        data = {
            'setting': request.POST.get('setting'),
            'description': request.POST.get('description'),
            'sh_desc': request.POST.get('sh_desc'),
            'lastuser': request.POST.get('lastuser')
        }
        response = requests.post(api_url, data=data)
        if response.status_code == 201:
            return redirect('./dis')
        else:
            return HttpResponse('Error creating setting')
    else:
        return render(request, 'setting_register/setting/setting_create.html')


def setting_edit(request, setting):
    # ------------------------------------------# ! ระวังลิ้งว่ามี / ไหม
    api_url = f'http://172.17.20.13/database/setting/{setting}'
    response = requests.get(api_url)
    if response.status_code == 200:
        setting = response.json()
        if request.method == 'POST':
            data = {
                'setting': request.POST.get('setting'),
                'description': request.POST.get('description'),
                'sh_desc': request.POST.get('sh_desc'),
                'lastuser': request.POST.get('lastuser')
            }
            response = requests.put(api_url, data=data)
            if response.status_code == 200:
                return redirect('../dis')  # ! ลิ้งกลับตาม url
            else:
                return HttpResponse('Error updating setting')
        else:
            return render(request, 'setting_register/setting/setting_edit.html', {'setting': setting})
    else:
        return HttpResponse('Setting not found')


def setting_delete(request, setting):
    api_url = f'http://172.17.20.13/database/setting/{setting}'
    response = requests.get(api_url)
    if response.status_code == 200:
        if request.method == 'POST':
            response = requests.delete(api_url)
            if response.status_code == 204:
                return redirect('/master/setting/dis')
            else:
                return HttpResponse('Error deleting setting')
        else:
            setting = response.json()
            return render(request, 'setting_register/setting/setting_delete.html', {'setting': setting})
    else:
        return HttpResponse('Setting not found')


def setting_detail(request, setting):
    # Make a GET request to the API endpoint with the ID of the setting to retrieve
    api_url = f'http://172.17.20.13/database/setting/{setting}'
    response = requests.get(api_url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        setting = response.json()
        return render(request, 'setting_register/setting/setting_detail.html', {'setting': setting})
    else:
        # Handle the error
        return HttpResponse('Error retrieving setting')

# ===========================================================================
#  !                              WARNING
#
#    test barcode scanner
#
#
# ===========================================================================
