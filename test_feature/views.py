from django.shortcuts import render,render_to_response 
from django.http import HttpResponse 
#from django.core.context_processors import request 
import json 
from .forms import AddForm

# Create your views here.

def index(request):
    if request.method == 'POST':
        form = AddForm(request.POST) 
        if form.is_valid():
            a = form.cleaned_data['a']
            b = form.cleaned_data['b']
            return HttpResponse(str(int(a) + int(b)))
     
    else:
        form = AddForm()
    return render(request, 'index.html', {'form': form})    
 
def add(request):
    a = request.GET['a']
    b = request.GET['b']
    a = int(a)
    b = int(b)
    return HttpResponse(str(a+b))


def Map(request): 
    return render_to_response("map.html") 
    #return HttpResponse("Hello!") 
      
Place_dict = { 
        "GuangDong":{ 
                        "GuangZhou":["PanYu","HuangPu","TianHe"], 
                        "QingYuan":["QingCheng","YingDe","LianShan"], 
                        "FoShan":["NanHai","ShunDe","SanShui"] 
                        }, 
        "ShanDong":{ 
                        "JiNan":["LiXia","ShiZhong","TianQiao"], 
                        "QingDao":["ShiNan","HuangDao","JiaoZhou"] 
                        }, 
        "HuNan":{ 
                        "ChangSha":["KaiFu","YuHua","WangCheng"], 
                        "ChenZhou":["BeiHu","SuXian","YongXian"] 
                    } 
    }; 
def Return_City_Data(request): 
    province = request.GET['Province'] 
    print province 
    City_list = [] 
    for city in Place_dict[province]: 
        City_list.append(city) 
    return HttpResponse(json.dumps(City_list))    
      
def Return_Country_Data(request): 
    province,city = request.GET['Province'],request.GET['City'] 
    print province,city 
    Country_list = Place_dict[province][city] 
    return HttpResponse(json.dumps(Country_list))

def category_manage(request):
    if request.GET.has_key('mode'):
        mode = request.GET['mode']
        if mode == 'reset':
            jfile = codecs.open('static/js/category_data.js','w','utf-8')
            jfile.write("var array=new Array();\n")
            clist = Category.objects.all()
            for c in clist:
                jfile.write ("array[%d]=new Array('%d','%d','%s')\n"%(c.id-1,c.id,c.c_father,c.c_name))
            jfile.close()
    return render_to_response('category_list.html',locals())

