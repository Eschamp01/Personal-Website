import os
import openai
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
import pdb

def index(request):
    return render(request, 'chatbot/index.html')

@csrf_exempt
def chatbot(request):
    if request.method == 'POST':
        print("post method activated!")
        message = request.POST.get('message', '')
        # Call the OpenAI API to generate a response
        openai.api_key = os.environ.get('OPENAI_API_KEY')
        response = openai.Completion.create(
            engine='text-davinci-003',
            prompt=message,
            max_tokens=1000,
            temperature=0.7
        )
        # Extract the generated response from the OpenAI API
        chatbot_response = response.choices[0].text.strip()
        return JsonResponse({'response': chatbot_response})
    else:
        return render(request, 'chatbot/index.html')
