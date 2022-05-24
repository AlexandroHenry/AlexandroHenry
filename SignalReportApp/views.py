from django.shortcuts import render, HttpResponse, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from SignalReportApp.models import SignalReport
from SignalReportApp.serializers import SignalReportSerializer
from rest_framework.decorators import api_view

# Create your views here.

def index(request):
    last_two_signalReports = SignalReport.objects.order_by('-created_at')[:2]
    
    return render(request, "alexandroHenry/home.html", {'latestReports': last_two_signalReports})

@csrf_exempt
def signalCreate(request):
    if request.method == 'GET':
        return render(request, "alexandroHenry/signalReportsWrite.html")
    elif request.method == 'POST':
        title = request.POST['title']
        body = request.POST['body']

        report_data = {'title': title, 'body': body}

        print(report_data)
        signalReport_serializer = SignalReportSerializer(data=report_data)
        if signalReport_serializer.is_valid():
            signalReport_serializer.save()
            # return JsonResponse(signalReport_serializer.data, status=status.HTTP_201_CREATED)
            return redirect('/')
        return JsonResponse(signalReport_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        








