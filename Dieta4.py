# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 17:39:32 2015

@author: viniciusra
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




################ Importações de Arquivos #####################################


alimentos = open ('alimentos.csv', 'r+')
x = alimentos.readlines()

usuario = open ('usuario1.csv','r+')
y = usuario.readlines()

##############################################################################




################## Informações Nutricionais/ Datas ###########################

quantidade = {}

calorias = {}

proteínas = {}

carboidratos = {}
    
gorduras = {}

data ={}





for i in x:
    comida = i.strip().split(',')
    quantidade[comida[0]] = comida[1]
    calorias[comida[0]] = comida[2]
    proteínas[comida[0]] = comida[3]
    carboidratos[comida[0]] = comida[4]
    gorduras[comida[0]] = comida[5]
    

#print (quantidade)    
#print (calorias)
#print (proteínas)
#print (carboidratos)
#print (gorduras)



for j in range(3,len(y)):
    caneta = y[j].strip().split(',')
    if caneta[0] not in data:
        data[caneta[0]] = [[caneta[1],caneta[2]]]
    else:
        data[caneta[0]] += [[caneta[1],caneta[2]]]
                
 
#print (data)

#############################################################################



################## Dados do usuário #########################################



dados = y[1].split(',')
nome = dados[0]
idade = int(dados[1])
peso = int(dados[2])
sexo = dados[3]
altura = float(dados[4])
fator_exercicios = dados[5]






##############################################################################




###### Regras de 3 para as quantidades ingeridas #############################

for x in data['06/04/15']:
    y = x[0]
    z = x[1]
    c = float(calorias[y])
    i = float (z)
    r = c*i/100
    print(y,'-',  'calorias(kcal):'  ,r)
    
    
    
for x in data['06/04/15']:
    y = x[0]
    z = x[1]
    c = float(proteínas[y])
    i = float (z)
    r = c*i/100
    print(y,'-',  'proteínas(g):'  ,r)
    
    
    
    
for x in data['06/04/15']:
    y = x[0]
    z = x[1]
    c = float(carboidratos[y])
    i = float (z)
    r = c*i/100
    print(y,'-',  'carboidratos(g):'  ,r)
    
    
    
for x in data['06/04/15']:
    y = x[0]
    z = x[1]
    c = float(gorduras[y])
    i = float (z)
    r = c*i/100
    print(y,'-',  'gorduras(g):'  ,r)
    
    
    
    
for x in data['07/04/15']:
    y = x[0]
    z = x[1]
    c = float(calorias[y])
    i = float (z)
    r = c*i/100
    print(y,'-',  'calorias(kcal):'  ,r)
    
    
    
    
for x in data['07/04/15']:
    y = x[0]
    z = x[1]
    c = float(proteínas[y])
    i = float (z)
    r = c*i/100
    print(y,'-',  'proteínas(g):'  ,r)
    
    
    
    
    
for x in data['07/04/15']:
    y = x[0]
    z = x[1]
    c = float(carboidratos[y])
    i = float (z)
    r = c*i/100
    print(y,'-',  'carboidratos(g):'  ,r)
    
    
    
    
    
for x in data['07/04/15']:
    y = x[0]
    z = x[1]
    c = float(gorduras[y])
    i = float (z)
    r = c*i/100
    print(y,'-',  'gorduras(g):'  ,r)
    


########## Contas ############################################################



def TMBHomens (peso,altura,idade):
    TMB = 88.36 + (13.4*peso) + (4.8*altura) - (5.7*idade)
    return TMBHomens


def TMBMulheres (peso,altura,idade):
    TMB = 447.6 + (9.2*peso) + (3.1*altura) - (4.3*idade)
    return TMBMulheres
    
    
dic = {}

dic["minimo"] = 1.2
dic["baixo"] = 1.375
dic['medio'] = 1.55
dic ['alto'] = 1.725
dic ['muito alto'] = 1.9


#if sexo == M :
#    if fator_exercicios == minimo:
#        TMBHomens()*dic['minimo']
#    elif fator_exercicios == baixo:
#        TMBHomens()*dic['baixo']






#print (dic)

      
#calorias_homens = TMBHomens(peso,altura,idade) * dic()
#
#calorias_mulheres = TMBMulheres(peso,altura,idade) *dic
#    