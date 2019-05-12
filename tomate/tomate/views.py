from django.shortcuts import render_to_response

#定义开始页面
def Home(request):
    context ={}
    return render_to_response("home.html", context)