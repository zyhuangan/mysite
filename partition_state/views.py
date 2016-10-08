#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse

from django.template import loader
from .models import t_apk_system_config
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

import os
import sys
import xlwt
import json
from optparse import OptionParser
import common as common

reload(sys)
sys.setdefaultencoding('utf-8')

COUNT_SIZE_PATH="/mnt/release_nfs/Count_Size/count_size/"
PROJECT_RESULT_XLS="compare_count_system.xls"

RETURN_UNKNOW=-99


def Return_Project_Data(request):
    platform = request.GET['platform']
    print "platform=%s"%(platform)
    project_list = []
    project_list = common.get_all_project(COUNT_SIZE_PATH,platform_name=platform)
    return HttpResponse(json.dumps(project_list))

def Return_Version_Data(request):
    platform_name = request.GET['platform']
    project_name = request.GET['project']
    print "platform_name=%s"%(platform_name)
    print "project_name=%s"%(project_name)
    version_list = common.get_all_version(COUNT_SIZE_PATH,platform_name=platform_name,project_name=project_name)
    return HttpResponse(json.dumps(version_list))

    
def httpResponse(status):
    result={"respCode":status}
    result=json.dumps(result)
    return HttpResponse(result)
'''
function index is used for to display Website home page.
'''
def index(request):
	context = {
		'title':'vivo',
		'site_title':'partition_state',
		}
	system_list = t_apk_system_config.objects.order_by('project')
	template = loader.get_template('partition_state/base_site.html')

	return HttpResponse(template.render(context,request))

'''
function show_check_partition is used for to display the all projects
partition information in show_check_partition html.
'''    
def show_check_partition(request):
    search_p = request.GET.get("p") if request.GET.get("p") else None
    all_system_list = t_apk_system_config.objects.order_by('project')
    print "search_p=%s"%(type(search_p))
    if search_p:
        system_list = t_apk_system_config.objects.filter(project=search_p)
        print "system_list=%s"%(system_list)
    else:
        system_list = all_system_list
    project_names_list=[]
    for i in all_system_list:
        project_name=i.project
        if project_name not in project_names_list:
            project_names_list.append(project_name)

    template = loader.get_template('partition_state/show_check_partition.html')
    context={
            'project_names_list':project_names_list,
            'system_list':system_list,
            'search_p':search_p,
        }
    #return render(request, 'partition_state/change_list.html', context)
    return HttpResponse(template.render(context,request))
    
def get_check_partition(request,project_name):
    all_system_list = t_apk_system_config.objects.order_by('project')
    if project_name:
        system_list = t_apk_system_config.objects.filter(project=project_name)
        print "system_list=%s"%(system_list)
    else:
        system_list = all_system_list
    project_names_list=[]
    for i in all_system_list:
        project_name=i.project
        if project_name not in project_names_list:
            project_names_list.append(project_name)

    template = loader.get_template('partition_state/show_check_partition.html')
    context={
            'project_names_list':project_names_list,
            'system_list':system_list,
        }
    #return render(request, 'partition_state/change_list.html', context)
    return HttpResponse(template.render(context,request))
    
'''
function show_newest_version_partition is used for to display the newest version of
projects partition information in show_newest_version_partition html.
'''   
def show_newest_version_partition(request):
    system_list = t_apk_system_config.objects.order_by('project')
    project_names_list=[]
    for i in system_list:
        project_name=i.project
        if project_name not in project_names_list:
            project_names_list.append(project_name)
    newest_version_objects = common.project_newest_version(project_names_list,system_list)
    template = loader.get_template('partition_state/show_newest_version_partition.html')
    context={
            'system_list':newest_version_objects,
            'project_names_list':project_names_list,
            }
    return HttpResponse(template.render(context,request))
    
def get_newest_version_partition(request):
    system_list = t_apk_system_config.objects.order_by('project')
    project_names_list=[]
    for i in system_list:
        project_name=i.project
        if project_name not in project_names_list:
            project_names_list.append(project_name)
    newest_version_objects = common.project_newest_version(project_names_list,system_list)
    print "newest_version_objects=%s"%(newest_version_objects)
    workbook=xlwt.Workbook(encoding="UTF-8")
    sheet=workbook.add_sheet('Sheet1')
    sheet.write(0,0,'项目')
    sheet.write(0,1,'版本')
    sheet.write(0,2,'system使用')
    sheet.write(0,3,'system总共')
    sheet.write(0,4,'system剩余')
    for i in range(len(newest_version_objects)):
        sheet.write(i+1,0,newest_version_objects[i].project)
        sheet.write(i+1,1,newest_version_objects[i].version)
        sheet.write(i+1,2,newest_version_objects[i].systemsize)
        sheet.write(i+1,3,newest_version_objects[i].fixedsize)
        sheet.write(i+1,4,newest_version_objects[i].surplussize)
    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename=newest_version_info.xls'
    workbook.save(response)
    return response


'''
function show_detail_partition is used for to display the detal information of one of project
version in show_detail_partition html.
'''  
def show_detail_partition(request):
    print "request.method=%s"%(request.method)
    project_names_list=[]
    versioninfo = []
    platform_list = common.get_all_platform(COUNT_SIZE_PATH)
    system_list = t_apk_system_config.objects.order_by('project')
    for i in system_list:
        project_name=i.project
        if project_name not in project_names_list:
            project_names_list.append(project_name)
    if request.method == 'GET':
        print "1111111111"
        platform_name = request.GET.get('platform_name', None)
        project_name = request.GET.get('project_name', None)
        version_name = request.GET.get('version_name', None)
        count_size_full_txt = COUNT_SIZE_PATH + str(platform_name) + '/' + str(project_name) + '/' + str(version_name) + '_count_size.txt'
        print "count_size_full_txt=%s"%(count_size_full_txt)
        if os.path.exists(count_size_full_txt):
            work_dic,key_list,value_list = common.check_system_details(count_size_full_txt)
            key_value_dic = common.list_to_dict(key_list, value_list)
            versioninfo += [platform_name, project_name, version_name]
        else:
            key_value_dic={}
            work_dic={}
        context={
            'system_list':system_list,
            'project_names_list':project_names_list,
            'key_value_dic':key_value_dic,
            'platform_list':platform_list,
            'versioninfo':versioninfo,
            #'project_list':project_list,
            #'version_obj':version_obj,
            }
        context.update(work_dic)
    else:
        context={
                'system_list':system_list,
                'project_names_list':project_names_list,
                'platform_list':platform_list,
                }
    template = loader.get_template('partition_state/show_detail_partition.html')
    #template = loader.get_template('partition_state/test.html')
    return HttpResponse(template.render(context,request))

'''
function show_compare_partition is used for to display the compare detal information of two
of project version in show_compare_partition html.
'''  
def show_compare_partition(request):
    platform_list = common.get_all_platform(COUNT_SIZE_PATH)
    project_list = common.get_all_project(COUNT_SIZE_PATH)
    version_obj = t_apk_system_config.objects.filter(project='PD1515BA')
    count_size_full_path1="/mnt/release_nfs/Count_Size/count_size/MSM8976IMG/PD1515BA/PD1515BA_A_1.18.1_count_size.txt"
    count_size_full_path2="/mnt/release_nfs/Count_Size/count_size/MSM8976IMG/PD1515BA/PD1515BA_A_1.18.2_count_size.txt"
    title_list,sum_dict,info_dict = common.compare_details_info(count_size_full_path1,count_size_full_path2)
    print "title_list=%s"%(title_list)
    print "sum_dict=%s"%(sum_dict)
    print "info_dict=%s"%(info_dict)
    system_list = t_apk_system_config.objects.order_by('project')
    project_names_list=[]
    for i in system_list:
        project_name=i.project
        if project_name not in project_names_list:
            project_names_list.append(project_name)
    context={
            'title_list':title_list,
            'info_dict':info_dict,
            'project_names_list':project_names_list,
            'platform_list':platform_list,
            'project_list':project_list,
            'version_obj':version_obj,
            }
    context.update(sum_dict)
    template = loader.get_template('partition_state/show_compare_partition.html')
    return HttpResponse(template.render(context,request))
    
def get_detail_partition(request, platform_name, project_name, version_name):
    #project_name = "PD1515BA"
    #version_name = "PD1515BA_A_1.18.1"
    try:
        count_size_full_txt = COUNT_SIZE_PATH + platform_name + '/' + project_name + '/' + version_name + '_count_size.txt'
        print count_size_full_txt
        if not os.path.exists(count_size_full_txt):
            print "error: the file %s is not exist"%(count_size_full_txt)
            return httpResponse(RETURN_UNKNOW)
        work_dic,key_list,value_list = common.check_system_details(count_size_full_txt)

        workbook=xlwt.Workbook(encoding="UTF-8")
        sheet=workbook.add_sheet('Sheet1')
        sheet.write(0,0,'文件')
        sheet.write(0,1,'大小')
        sheet.write(1,0,work_dic.keys())
        sheet.write(1,1,work_dic.values())
        i=2
        for k in range(len(key_list)):
            file_name=key_list[k]
            file_size=value_list[k]
            sheet.write(i,0,file_name)
            sheet.write(i,1,file_size)
            i=i+1
        
        response = HttpResponse(content_type='application/vnd.ms-excel')
        response['Content-Disposition'] = 'attachment; filename=check_details_info.xls'
        workbook.save(response)
        return response
    except Exception as e:
        print e
        return httpResponse(RETURN_UNKNOW)
    
def compare_partition(request):
    try:
        platfrom1=request.GET.get("platfrom1") if request.GET.get("platfrom1") else None
        project1=request.GET.get("project1") if request.GET.get("project1") else None
        version1=request.GET.get("version1") if request.GET.get("version1") else None
        platfrom2=request.GET.get("platfrom2") if request.GET.get("platfrom2") else None
        project2=request.GET.get("project2") if request.GET.get("project2") else None
        version2=request.GET.get("version2") if request.GET.get("version2") else None
        if not platfrom1 or \
           not platfrom2 or \
           not project1 or \
           not project2 or \
           not version1 or \
           not version2:
            print "error:param error"
            sys.exit(0)
        count_size_full_path1=COUNT_SIZE_PATH+platfrom1+'IMG/'+project1+'/'+version1+'_count_size.txt'
        count_size_full_path2=COUNT_SIZE_PATH+platfrom2+'IMG/'+project2+'/'+version2+'_count_size.txt'
        if not os.path.exists(count_size_full_path1):
            print "error: the file %s is not exist"%(count_size_full_path1)
            sys.exit(1)
        if not os.path.exists(count_size_full_path2):
            print "error: the file %s is not exist"%(count_size_full_path2)
            sys.exit(1)
        title_list,sum_dict,info_dict = common.compare_details_info(count_size_full_path1,count_size_full_path2)
        workbook = common.WriteToXls(PROJECT_RESULT_XLS,title_list, sum_dict, info_dict)
        
        response = HttpResponse(content_type='application/vnd.ms-excel')
        response['Content-Disposition'] = 'attachment; filename=compare_count_system.xls'
        workbook.save(response)
        return response
        
    except Exception as e:
        print e
        return httpResponse(RETURN_UNKNOW)
        
#python check_details_info.py -p MSM8976 -x PD1522A -v 1.17.2 -h MA
def detail_partition(request):
    try:
        platform_name=request.GET.get("platfrom") if request.GET.get("platfrom") else None
        project_name=request.GET.get("project") if request.GET.get("project") else None
        version=request.GET.get("version") if request.GET.get("version") else None
        hdware=request.GET.get("hdware") if request.GET.get("hdware") else None
        if not platform_name or not project_name or not version or not hdware:
            return httpResponse(RETURN_UNKNOW)
        if not 'MT' and 'MSM' in platform_name:
            return httpResponse(RETURN_UNKNOW)
        count_size_full_path=COUNT_SIZE_PATH+platform_name+'IMG/'+project_name
        if 'MA' in hdware:
            hdware_name='A'
        elif 'MB' in hdware:
            hdware_name='B'
        count_size_full_txt=count_size_full_path+'/'+project_name+'_'+hdware_name+'_'+version+'_count_size.txt'
        print count_size_full_txt
        if not os.path.exists(count_size_full_txt):
            print "error: the file %s is not exist"%(count_size_full_txt)
            return httpResponse(RETURN_UNKNOW)
        work_dic,key_list,value_list = common.check_system_details(count_size_full_txt)
        
        workbook=xlwt.Workbook(encoding="UTF-8")
        sheet=workbook.add_sheet('Sheet1')
        sheet.write(0,0,'文件')
        sheet.write(0,1,'大小')
        sheet.write(1,0,work_dic.keys())
        sheet.write(1,1,work_dic.values())
        i=2
        for k in range(len(key_list)):
            file_name=key_list[k]
            file_size=value_list[k]
            sheet.write(i,0,file_name)
            sheet.write(i,1,file_size)
            i=i+1
        
        response = HttpResponse(content_type='application/vnd.ms-excel')
        response['Content-Disposition'] = 'attachment; filename=check_details_info.xls'
        workbook.save(response)
        return response
    except Exception as e:
        print e
        return httpResponse(RETURN_UNKNOW)
        
def check_partition(request, project_name):
    #project_name = request.GET.get("project") if request.GET.get("project") else None
    arraylist = common.GetPartitionInfo(project_name)
    print "arraylist=%s"%(arraylist)
    try:
        workbook=xlwt.Workbook(encoding="UTF-8")
        sheet=workbook.add_sheet("Sheet1")
        sheet.write(0,0,"id")
        sheet.write(0,1,"项目名")
        sheet.write(0,2,"版本号")
        sheet.write(0,3,"分区使用大小")
        sheet.write(0,4,"分区固定大小")
        sheet.write(0,5,"分区剩余大小")
        #sheet.write(0,6,"硬件版本号")
        for i in range(len(arraylist)):
          id=arraylist[i][0]
          project=arraylist[i][1]
          version=arraylist[i][2]
          systemSize=arraylist[i][3]
          fixedSize=arraylist[i][4]
          surplusSize=arraylist[i][5]
          #hdversion=arraylist[i][6]
          
          sheet.write(i+1,0,id)
          sheet.write(i+1,1,project)
          sheet.write(i+1,2,version)
          sheet.write(i+1,3,systemSize)
          sheet.write(i+1,4,fixedSize)
          sheet.write(i+1,5,surplusSize)
          #sheet.write(i+1,6,hdversion)
    except Exception as e:
        print "error:WriteToXls",e
    finally:
        response = HttpResponse(content_type='application/vnd.ms-excel')
        response['Content-Disposition'] = 'attachment; filename=check_count.xls'
        workbook.save(response)
        return response

'''
function get_all_partition is used for downloading all the projects partition
information from database.
'''
def get_all_partition(request):
    system_list = t_apk_system_config.objects.order_by('project')
    workbook=xlwt.Workbook(encoding="UTF-8")
    sheet=workbook.add_sheet("Sheet1")
    sheet.write(0,0,"id")
    sheet.write(0,1,"项目名")
    sheet.write(0,2,"版本号")
    sheet.write(0,3,"分区使用大小")
    sheet.write(0,4,"分区固定大小")
    sheet.write(0,5,"分区剩余大小")
    i = 0
    for system in system_list:
        sheet.write(i+1,0,system.id)
        sheet.write(i+1,1,system.project)
        sheet.write(i+1,2,system.version)
        sheet.write(i+1,3,system.systemsize)
        sheet.write(i+1,4,system.fixedsize)
        sheet.write(i+1,5,system.surplussize)
        i+=1
    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename=all_partition.xls'
    workbook.save(response)
    return response
