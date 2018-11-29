/*ajax请求工具类*/
function getParams(dict){
    var params=""
    if(dict){
        params="?"
        for(i in  dict){
            params+=i+"="+dict[i]+"&";
        }
    }
    return params;
}
var exceptInfo={"404":"资源不存在！","500":"服务器异常！","403":"访问被拒绝！","502":"网关错误！"}
function ajax_send(path,args,method,obj){
    var xhr;
    var resultData;
    if(window.ActiveXObject){
        xhr=new ActiveXObject("Micrsoft.XMLHTTP");
    }else if (window.XMLHttpRequest){//webkit IE7
        xhr=new XMLHttpRequest()
    }
    var params=getParams(args);
    console.log(path,params);
    if(method=='GET' || method=='get'){
        xhr.open(method,path+params)
        xhr.send()
    }else{
        xhr.open(method,path)
        var csrftoken = "{{csrf_token}}"; //获取csrf的校验令牌
        xhr.setRequestHeader("X-CSRFToken", csrftoken); //将令牌放在请求头中
        xhr.setRequestHeader("content-type", "application/x-www-form-urlencoded");
        xhr.send(params)
    }
    obj.attr("src","/static/img/ajax/load.gif");
    xhr.onreadystatechange=function () {
        if(xhr.readyState == 4){
            if(xhr.status==200){
                obj.css("display","inline-block");
                if(xhr.responseText=="1"){
                    obj.attr("src","/static/img/ajax/error.jpg");
                    $("#checkval").val("n")
                }else{
                    obj.attr("src","/static/img/ajax/ok.gif");
                    $("#checkval").val("y")
                }


            }else{
                for(i in exceptInfo){
                    if(xhr.status==parseInt(i)){
                        obj.text(exceptInfo[i]);
                    }
                }
            }
        }else{
           obj.text("未知异常！");
        }
    }
}
