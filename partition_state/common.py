#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import re
import sys
import xlwt
import time
import shutil
import zipfile
import tempfile
import string
import json
import MySQLdb
import subprocess

from .models import t_apk_system_config
reload(sys)
sys.setdefaultencoding('utf-8')

PROJECT_RESULT_XLS="compare_count_system.xls"

def execCmdWithOutput(cmd):                                                                                                      
    output = ""
    error = 1 
    try:
        p = subprocess.Popen(cmd, stdout = subprocess.PIPE, stderr = subprocess.PIPE, shell = True)
        output, error = p.communicate()
        p.wait()
    except Exception as e:
        print "error:",e
    return output, error

def sortedDictKey(adict):
  new_keys=[]
  new_values=[]
  keys=adict.keys()
  keys.sort()
  for i in keys:
    new_keys.append(i)
    new_values.append(adict[i])
  return new_keys,new_values
  
def check_system_details(txtfile):
  work_list=[]
  work_dic1={}
  work_dic2={}
  key_list=[]
  value_list=[]
  f=open(txtfile)
  lines=f.readlines()
  f.close
  first_number=lines.index('system\n')
  last_number=lines.index('data\n')
  work_lines=lines[first_number:last_number]

  assert(work_lines[0]=='system\n')
  work_dic1[work_lines[0].strip()]=work_lines[1].strip()
  
  for line in work_lines[2:]:
    work_list.append(line.strip('\n').strip(' '))

  for line in work_list:
    line=' '.join(line.split())
    if not '/' in line:
      work_dic2[line.split(' ')[0]]=line.split(' ')[1]

  key_list,value_list=sortedDictKey(work_dic2)
  return work_dic1,key_list,value_list

def get_json_of_compare(project_name_list,title_list,sum_dict,info_dict):
#WriteToXls(PROJECT_RESULT_XLS,title_list, sum_dict, info_dict)
  json_info={}
  partition_info={}
  
  json_info['project_name']=project_name_list
  json_info['version']=title_list
  json_info['partition_name']=sum_dict
  json_info['partition_info']=info_dict
  
  jsonStr = json.dumps(json_info) 
  
  print "jsonStr:",jsonStr 
  
def WriteToXls(xlsfile,title_list, sum_dict, info_dict):
  if os.path.exists(xlsfile):
    os.remove(xlsfile)
  try:
    workbook=xlwt.Workbook(encoding="UTF-8")
    sheet=workbook.add_sheet("Sheet1")
    sheet.write(0,0,"软件版本")
    sheet.write(0,1,title_list[0])
    sheet.write(0,2,title_list[1])
    
    sheet.write(1,0,sum_dict.keys()[0])
    sheet.write(1,1,sum_dict.values()[0][0])
    sheet.write(1,2,sum_dict.values()[0][1])
    
    i=2
    for k in range(len(info_dict)):
      sheet.write(i,0,info_dict.keys()[k])
      sheet.write(i,1,info_dict.values()[k][0])
      sheet.write(i,2,info_dict.values()[k][1])
      i=i+1
      
  except Exception as e:
    print "error:WriteToXls",e
  finally:
    #workbook.save(xlsfile)
    return workbook
    
def compare_details_info(txtfile1,txtfile2):
  project_name_list=[]
  title_list=[]
  system_dict1={}
  system_dict2={}
  key_list1=[]
  key_list2=[]
  value_list1=[]
  value_list2=[]
  sum_dict={}
  info_dict={}
  title_list.append(os.path.basename(txtfile1).split('_count_size.txt')[0])
  title_list.append(os.path.basename(txtfile2).split('_count_size.txt')[0])
  project_name_list.append(os.path.basename(txtfile1).split('_count_size.txt')[0].split("_")[0])
  project_name_list.append(os.path.basename(txtfile2).split('_count_size.txt')[0].split("_")[0])
  system_dict1,key_list1,value_list1=check_system_details(txtfile1)
  system_dict2,key_list2,value_list2=check_system_details(txtfile2)
  if not len(system_dict1)==len(system_dict2) \
        or not len(key_list1)==len(value_list1) \
        or not len(key_list2)==len(value_list2):
    print "error:txtfile error"
    Usage()
    sys.exit(0)

  for i in system_dict1.keys():
    sum_dict[i]=[system_dict1[i],system_dict2[i]]
  for i in range(len(key_list1)):
    for j in range(len(key_list1)):
      if key_list1[i]==key_list2[j]:
        info_dict[key_list1[i]]=[value_list1[i],value_list2[j]]
  return title_list,sum_dict,info_dict
  #WriteToXls(PROJECT_RESULT_XLS,title_list, sum_dict, info_dict)
  #common.get_json_of_compare(project_name_list,title_list,sum_dict,info_dict)

def sortedDictValue(adict):
  key_list=[]
  value_list=[]
  new_dict={}
  new_keys=[]
  new_values=[]
  for key,value in adict.items():
    key_list.append(key)
    value_list.append(value)
    
  for i in adict.keys():
    new_dict[i]=adict[i][:-1]
  new_values=new_dict.values()
  new_values.sort(reverse=True)
  print new_values
  for i in new_values:
    get_value_index=value_list.index(i+'M')
    new_keys.append(key_list[get_value_index])
  for i in range(len(new_values)):
    new_values[i]=new_values[i]+'M'
  return new_keys,new_values
  
def check_system_details(count_size_txt):
  work_list=[]
  work_dic1={}
  work_dic2={}
  key_list=[]
  value_list=[]
  f=open(count_size_txt)
  lines=f.readlines()
  f.close
  first_number=lines.index('system\n')
  last_number=lines.index('data\n')
  work_lines=lines[first_number:last_number]
  
  assert(work_lines[0]=='system\n')
  work_dic1[work_lines[0].strip()]=work_lines[1].strip()
  
  for line in work_lines[2:]:
    work_list.append(line.strip('\n').strip(' '))
  for line in work_list:
    line=' '.join(line.split())
    if not '/' in line:
      work_dic2[line.split(' ')[0]]=line.split(' ')[1]
  #key_list,value_list=sortedDictKey(work_dic2)
  key_list,value_list=sortedDictValue(work_dic2)
  #get_json_of_info(OPTIONS.project_name,OPTIONS.version,work_dic1,key_list,value_list)
  #WriteToXls(PROJECT_RESULT_XLS,work_dic1,key_list,value_list)
  return work_dic1,key_list,value_list
  
def GetPartitionInfo(project):
    #HOST="172.20.125.244"
    HOST="192.168.2.177"
    USER="root"
    PASSWORD="bbk12345"
    DATABASE="new_bbgcms"
    arraylist=[]
    conn=MySQLdb.connect(host=HOST,user=USER,passwd=PASSWORD,db=DATABASE,charset="utf8")
    cur=conn.cursor()
    sql="select * from t_apk_system_config where project='%s'"%(project)
    number=cur.execute(sql)
    info=cur.fetchmany(number)
    cur.close()
    conn.commit()
    conn.close()
    
    for i in info:
      arraylist.append(list(i))
    if len(arraylist)==0:
      print "error: there is no count info of %s"%(project)
    return arraylist

'''
fuction cmpVersion is used for comparing the versions like 1.1.1,
and get the new list the versions from big to small
'''
def cmpVersion(arraylist):
    originlist=arraylist
    for i in arraylist:
        match = re.match(r'.*[a-zA-Z].*', i)
        if bool(match):
            originlist.remove(i)
    #print table.cell_value(0,j+1).split('.')
    for i in range(len(originlist)-1,0,-1):
        for z in range(i):
            if int(originlist[z].split('.')[0]) < int(originlist[z+1].split('.')[0]):
                temp=originlist[z]
                originlist[z]=originlist[z+1]
                originlist[z+1] = temp
            elif int(originlist[z].split('.')[0])==int(originlist[z+1].split('.')[0]):
                if int(originlist[z].split('.')[1]) < int(originlist[z+1].split('.')[1]):
                    temp=originlist[z]
                    originlist[z]=originlist[z+1]
                    originlist[z+1] = temp
                elif int(originlist[z].split('.')[1])==int(originlist[z+1].split('.')[1]):
                    if int(originlist[z].split('.')[2])<int(originlist[z+1].split('.')[2]):
                        temp=originlist[z]
                        originlist[z]=originlist[z+1]
                        originlist[z+1] = temp
    return originlist

'''
fuction project_newest_version is used for get the newset version information every project
and return the object.
''' 
def project_newest_version(project_names_list,system_list):
    newest_version_objects = []
    for i in project_names_list:
        project_objects = t_apk_system_config.objects.filter(project=i)
        version_list_before = []
        for j in project_objects:
            version_list_before.append(str(j.version))
        print "i=%s"%(i)
        print "version_list_before=%s"%(version_list_before)
        version_list_after = cmpVersion(version_list_before)
        print "version_list_after=%s"%(version_list_after)
        newest_version = version_list_after[0]
        newest_version_object = t_apk_system_config.objects.filter(project=i).filter(version=newest_version)
        newest_version_objects += newest_version_object
    return newest_version_objects

def list_to_dict(arraylist1, arraylist2):
    dict = {}
    if len(arraylist1) != len(arraylist2):
        return dict
    for i in range(len(arraylist1)):
        dict[arraylist1[i]] = arraylist2[i]
    return dict

def get_all_platform(work_path):
    platform_list = []
    if not os.path.exists(work_path):
        return platform_list
    platform_list = os.listdir(work_path)
    return platform_list

def get_all_project(work_path,platform_name='MSM8976IMG'):
    project_list = []
    if not os.path.exists(os.path.join(work_path, platform_name)):
        return project_list
    project_list = os.listdir(os.path.join(work_path, platform_name))
    return project_list

def get_all_version(work_path,platform_name='MSM8976IMG',project_name="PD1515BA"):
    version_list = []
    work_dir = work_path + platform_name + '/' + project_name
    if not os.path.exists(work_dir):
        return version_list
    cmd = 'ls ' + work_dir + ' | awk -F \'_count_size.txt\' \'{print $1}\''
    output,error=execCmdWithOutput(cmd)
    if not error:
        version_list = output.split("\n")
    return version_list

'''
fuction get_platform_project_version_information_dic is used for getting the dict
of about the information of platform project and version. like json
'''
def get_platform_project_version_information_dic(work_path):
    info_dict = {}
    project_dict = {}
    version_list = []
    all_platform = get_all_platform(work_path)
    for platform_name in all_platform:
        all_project = get_all_project(work_path,platform_name=platform_name)
        for project_name in all_project:
            project_path = work_path + platform_name + '/' + project_name
            cmd = 'ls ' + project_path + ' | awk -F \'_count_size.txt\' \'{print $1}\''
            print "cmd=%s"%(cmd)
            output,error=execCmdWithOutput(cmd)
            if not error:
                version_list = output.split("\n")
                project_dict[project_name]=version_list
        info_dict[platform_name]=project_dict
    return info_dict