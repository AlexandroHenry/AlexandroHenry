from rest_framework import serializers
from SignalReportApp.models import SignalReport

class SignalReportSerializer(serializers.ModelSerializer):

    class Meta:
        model = SignalReport
        fields = ('id',
                  'title',
                  'body'
                  )