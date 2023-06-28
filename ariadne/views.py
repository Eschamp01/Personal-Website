from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from . import openai_api
import json
import ast
import pdb

def index(request):
    return render(request, 'ariadne/index.html')

def solver(request):
    return render(request, 'ariadne/solver.html')

def solve_problem(request):
    if request.method == "POST":

        hintCount = int(request.POST.get('hintCount'))
        assumptions = [request.POST.get(f'hint_{i}') for i in range(1, hintCount+1)]
        if hintCount == 0:
            assumptions = [""]

        problem_params_dict = {
            'problem' : request.POST.get('problem'),
            'method' : request.POST.get('method'),
            'assumptions' : assumptions,
        }

        use_list = True

        problem_steps = openai_api.break_down_problem(problem_params_dict, list=use_list)
        problem_steps = ast.literal_eval(problem_steps) if use_list else json.loads(problem_steps.replace("'", '"'))

        answers = openai_api.get_answers(problem_params_dict, problem_steps, list=use_list)
        answers = ast.literal_eval(answers) if use_list else json.loads(answers.replace("'", '"'))
        # Combine the two dictionaries into a list of tuples
        steps_and_answers = list(zip(problem_steps,answers)) if use_list else list(zip(problem_steps.values(), answers.values())) 

        result = {'steps_and_answers': steps_and_answers}
        # result = {
        #         'problem_steps': problem_steps,
        #         'answers': answers,
        #         }
        return render(request, 'ariadne/solver.html', result)

    return HttpResponse("The reauest was meant to be a POST request, but this one was not.")

def improved_index(request):
    return render(request, 'ariadne/improved_index.html')

def moon(request):
    return render(request, 'ariadne/moon.html')

def plane(request):
    return render(request, 'ariadne/plane.html')

def robots(request):
    return render(request, 'ariadne/robots.html')