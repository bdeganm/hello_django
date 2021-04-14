from django.shortcuts import render, HttpResponse

# Create your views here.

def hello(request, nome, idade):
    return HttpResponse('<h1>Hello {} de {} anos.</h1>'.format(nome, idade))

def soma(request, num1, num2):
    resultado = num1 + num2
    return HttpResponse('A soma de {} e {} é igual a {}'.format(num1, num2, resultado))

def subtracao(request, num1, num2):
    resultado = num1 - num2
    return HttpResponse('A subtração de {} por {} é igual a {}'.format(num1, num2, resultado))

def multiplicacao(request, num1, num2):
    resultado = num1 * num2
    return HttpResponse('O produto de {} e {} é igual a {}'.format(num1, num2, resultado))


def divisao(request, num1, num2):
    resultado = num1 / num2
    return HttpResponse('A divisão de {} por {} é igual a {}'.format(num1, num2, resultado))
