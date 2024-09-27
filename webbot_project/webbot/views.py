# webbot/views.py

from django.shortcuts import render
from .ml_model import predict


def index(request):
    return render(request, 'webbot/index.htm')


def bot_search(request):
    query = request.GET.get('query')

    if not query:
        return render(request, 'webbot/index.htm', {'ans': "Please enter a query.", 'query': query})

    try:
        # Make prediction using ML model
        prediction = predict(query)

        return render(request, 'webbot/index.htm', {'ans': prediction, 'query': query})

    except Exception as e:
        print(f"Error: {e}")
        ans = "Error fetching data."
        return render(request, 'webbot/index.htm', {'ans': ans, 'query': query})
