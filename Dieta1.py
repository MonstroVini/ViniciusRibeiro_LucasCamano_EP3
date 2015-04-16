# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 19:13:02 2015

@author: Vinícius Ribeiro
"""

"""
Fórmula de Harris - Benedict
Homens:
TMB = 88,36 + (13,4 x peso, kg) + (4,8 x altura, cm) - (5,7 x idade em anos)

Mulheres:
TMB = 447,6 + (9.2 x peso, kg) + (3,1 x altura, cm) - (4,3 x idade em anos)

Fator Atividade:
Grau mínimo, necessidade calórica = TMB x 1,2
Baixo, necessidade calórica = TMB x 1,375
Médio, necessidade calórica = TMB x 1,55
Alto, necessidade calórica = TMB x 1,725
Muito alto, necessidade calórica = TMB x 1,9

Calorias Diárias:

Calorias = TMB x Fator de Atividade

"""

alimentos = {}

quantidade = {}

calorias = {}

proteínas = {}

carboidratos = {}
    
gorduras = {}



alimentos = open ('alimentos.csv', 'r+')
x = alimentos.readlines()


usuario = open('usuario.csv', 'r+')
y = usuario.readlines()

alimentos_limpos = []

for i in x:
    i.strip().split()
    print(i)
    
    
for j in y:
    j.strip().split()
    print (j)
    

    
    
#nome = input ('Qual seu nome?\n')
#sexo = input ('Qual seu sexo?\n')
#peso = float(input('Qual seu peso em kg?\n'))
#altura = float(input('Qual sua altura em centímetros?\n'))
#idade = input('Qual sua idade em anos?\n')
#fator_atividade = input('Qual seu fator de atividade física?\n')

def TMBHomens (peso,altura,idade):
    TMB = 88.36 + (13.4*peso) + (4.8*altura) - (5.7*idade)
    return TMBHomens

def TMBMulheres (peso,altura,idade):
    TMB = 447.6 + (9.2*peso) + (3.1*altura) - (4.3*idade)
    return TMBMulheres
    
def GrauMinimo ():
    GrauMinimo = 1.2
    return GrauMinimo

def Baixo():
    Baixo = 1.375
    return Baixo
    
def Medio():
    Medio = 1.55 
    return Medio
    
def Alto ():
    Alto = 1.725
    return Alto
    
def MuitoAlto():
    MuitoAlto = 1.9
    return MuitoAlto
    
dic = {}

dic["minimo"] = 1.2
dic["baixo"] = 1.375
dic['medio'] = 1.55
dic ['alto'] = 1.725
dic ['muito alto'] = 1.9



if sexo == 'masculino':
    if fator_atividade == 'minimo':
        Calorias = TMBHomens(peso, altura, idade) * dic["baixo"]
        print (Calorias)
        
    













    





