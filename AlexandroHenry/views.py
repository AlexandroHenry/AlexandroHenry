from django.shortcuts import render, HttpResponse, redirect
from django.views.decorators.csrf import csrf_exempt

# def index(request):
#     return render(request, "alexandroHenry/home.html")

# @csrf_exempt
# def signalCreate(request):
#     if request.method == 'GET':
#         return render(request, "alexandroHenry/signalReportsWrite.html")
#     elif request.method == 'POST':
#         title = request.POST['title']
#         body = request.POST['body']
#         print(title,body)
#         return redirect('/')

