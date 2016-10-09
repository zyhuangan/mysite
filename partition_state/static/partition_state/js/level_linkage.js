//用来获得option元素中selected属性为true的元素的id 
function Get_Selected_Id(place){ 
    var pro = document.getElementById(place); 
    var Selected_Id = pro.options[pro.selectedIndex].id; 
    console.log("Get_Selected_Id:"+Selected_Id);  //测试使用 
    return Selected_Id;        //返回selected属性为true的元素的id 
} 

//执行相应的动作，调用相关数据请求函数 
function Get_Next_Place(This_Place_ID,Action,Num){ 
    var Selected_Id = Get_Selected_Id(This_Place_ID);  //Selected_Id用来记录当前被选中的省或市的ID 
    if(Action=='Get_project')                            //从而可以在下一个级联中加载相应的市或县 
        Get_Project_Data(Selected_Id, Num); 
    else if(Action=='Get_version') 
        Get_Version_Data(Selected_Id, Num); 
} 

//向服务器请求城市列表数据并调用添加城市函数 
function Get_Project_Data(Province_Selected_Id, Num){    //这里的Selected_Id应该是被选中的省份的ID 
    console.log("Province_Selected_Id:"+Province_Selected_Id);  //测试使用 
    if(Province_Selected_Id == 'Not_platform1'){    //如果选择了"Province"选项，则表示重置当前City和Country的选项内容，不会向服务器请求数据 
        $("#project1").empty(); 
        $("#project1").append("<option id='Not_project1'>Project</option>"); 
        $("#version1").empty(); 
        $("#version1").append("<option id='Not_version1'>Version</option>"); 
    }else if(Province_Selected_Id == 'Not_platform2'){
        $("#project2").empty(); 
        $("#project2").append("<option id='Not_project2'>Project</option>"); 
        $("#version2").empty(); 
        $("#version2").append("<option id='Not_version2'>Version</option>"); 
    }else{      //否则就会向服务器请求数据 
        $.getJSON('/partition_state/GetProjectData/',{'platform':Province_Selected_Id},function(project_list){ 
            console.log(project_list);      //测试使用 
            Add_project(Num, project_list);    //调用添加城市选项函数 
        }); 
    } 
} 

//在当前页面添加城市选项 
function Add_project(Num,project_list){ 
    if(Num == '1'){
        $("#project1").empty(); 
        $("#project1").append("<option id='Not_project1'>Project</option>"); 
        $("#version1").empty(); 
        $("#version1").append("<option id='Not_version1'>Version</option>"); 
        for(var index in project_list){    //获得城市列表中的城市索引 
            //添加内容的同时在option标签中添加对应的城市ID 
            var text = "<option"+" id='"+project_list[index]+"'>"+project_list[index]+"</option>"; 
            $("#project1").append(text); 
            console.log(text);  //用来观察生成的text数据 
        }
    } else if(Num == '2'){
        $("#project2").empty(); 
        $("#project2").append("<option id='Not_project2'>Project</option>"); 
        $("#version2").empty(); 
        $("#version2").append("<option id='Not_version2'>Version</option>"); 
        //上面的两次清空与两次添加是为了保持级联的一致性 
        for(var index in project_list){    //获得城市列表中的城市索引 
            //添加内容的同时在option标签中添加对应的城市ID 
            var text = "<option"+" id='"+project_list[index]+"'>"+project_list[index]+"</option>"; 
            $("#project2").append(text); 
            console.log(text);  //用来观察生成的text数据 
        } 
    }else{
        for(var index in project_list){
            var text = "<option"+" id='"+project_list[index]+"'>"+project_list[index]+"</option>"; 
            $("#project2").append(text); 
            console.log(text);
        } 
    }
} 

//向服务器请求县区列表数据并调用添加县区函数 
function Get_Version_Data(Project_Selected_Id, Num){ 
  console.log("Project_Selected_Id:"+Project_Selected_Id);  //测试使用 
  if(Project_Selected_Id == 'Not_project1'){    //如果选择了City选项，则表示重置当前Country的选项内容，不会向服务器请求数据 
      $("#version1").empty(); 
      $("#version1").append("<option id='Not_version1'>Version</option>"); 
      //上面的清空与添加是为了保持级联的一致性 
  }else{  //否则就会向服务器请求数据 
      var Platform_Selected_ID = Get_Selected_Id("platform1");   
      $.getJSON('/partition_state/GetVersionData/',{'platform':Platform_Selected_ID,'project':Project_Selected_Id},function(version_list){ 
          console.log(version_list);    //测试使用 
          Add_version(Num, version_list);  //调用添加县区选项函数 
      }); 
  } 
  if(Project_Selected_Id == 'Not_project2'){
      $("#version2").empty(); 
      $("#version2").append("<option id='Not_version2'>Version</option>"); 
  }else{
      var Platform_Selected_ID = Get_Selected_Id("platform2");   
      $.getJSON('/partition_state/GetVersionData/',{'platform':Platform_Selected_ID,'project':Project_Selected_Id},function(version_list){ 
          console.log(version_list);
          Add_version(Num, version_list);  
      }); 
  } 
} 

//在当前页面添加县区选项 
function Add_version(Num, version_list){ 
    if(Num == '1'){
        $("#version1").empty(); 
        $("#version1").append("<option id='Not_version1'>Version</option>"); 
        //上面的清空与添加是为了保持级联的一致性 
        for(var index in version_list){    //获得县区列表中的县区索引 
            //添加内容的同时在option标签中添加对应的城市ID 
            var text = "<option"+" id='"+version_list[index]+"'>"+version_list[index]+"</option>"; 
            $("#version1").append(text); 
            console.log(text);  //用来观察生成的text数据 
        } 
    }else if(Num == '2'){
        $("#version2").empty(); 
        $("#version2").append("<option id='Not_version2'>Version</option>"); 
        for(var index in version_list){
            var text = "<option"+" id='"+version_list[index]+"'>"+version_list[index]+"</option>"; 
            $("#version2").append(text); 
            console.log(text);
        } 
    }
} 
