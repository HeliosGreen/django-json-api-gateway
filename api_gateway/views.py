# api_gateway/views.py
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .service import DataService
from django.shortcuts import render

import json

def index(request):
    return render(request, 'index.html')

@csrf_exempt  # Only for demo purposes, you should handle CSRF properly in a real application
def save_data(request):
    if request.method == 'POST':
        data_id = request.POST.get('data_id')
        data_text = request.POST.get('data_text')
        DataService.add_data(data_id, data_text)
        return JsonResponse({'message': 'Data saved successfully'})

    return JsonResponse({'error': 'Invalid request method'}, status=400)

def view_data(request):
    data_from_service = DataService.get_all_data()
    return JsonResponse(data_from_service, safe=False)
