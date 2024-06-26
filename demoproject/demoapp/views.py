from django.shortcuts import render
from django.http import HttpResponse
# from datetime import datetime

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def home(request):
    path = request.path
    scheme = request.scheme
    method = request.method
    address = request.META['REMOTE_ADDR']
    user_agent = request.META['HTTP_USER_AGENT']
    path_info = request.path_info

    response =HttpResponse()
    response.headers['Age'] = 20

    msg = f"""<br>
    <br>Path : {path}
    <br>Adress : {address}
    <br>Scheme : {scheme}
    <br>Method :{method}
    <br>User agent : {user_agent}
    <br>path info : {path_info}
    <br> Response header : {response.headers}
  """
    return HttpResponse( msg,content_type = 'text/html',charset = 'utf-8')
  

#  def day_time(request):
 #   now = datetime.today().year
  #  return HttpResponse(now)

#def message(request):
 #   text = """<h1 style="color:#F4CE14;">Welcome to color changing django</h1>"""
  #  return HttpResponse(text)
# Create your views here.
