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

Fórmula de Nick Trefethen

IMC = 1,3 X peso (em quilogramas)/ altura^2,5tros)
Saudável : IMC = 18,5 - 24,9
Frangolino : IMC < 18,5
Sobrepeso: IMC = 25 - 29,9
Toda obesidade: IMC > 30
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

grafico_kcal = []

grafico_p = []

grafico_c = []

grafico_g = []






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


#print(nome)
#print(idade)
#print(peso)
#print(sexo)
#print(altura)
#print(fator_exercicios)





##############################################################################




###### Regras de 3 para as quantidades ingeridas #############################


calorias_06_abril = []

for x in data['06/04/15']:
    y = x[0]
    z = x[1]
    c = float(calorias[y])
    i = float (z)
    r = c*i/100
    calorias_06_abril.append(r)
#    print(y,'-',  'calorias(kcal):'  ,r)


grafico_kcal.append(sum(calorias_06_abril))
    
#print (grafico_kcal) 


proteínas_06_abril = []   
    
for x in data['06/04/15']:
    y = x[0]
    z = x[1]
    c = float(proteínas[y])
    i = float (z)
    r = c*i/100
    proteínas_06_abril.append(r)
#    print(y,'-',  'proteínas(g):'  ,r)
    
grafico_p.append(sum(proteínas_06_abril))
    



carboidratos_06_abril = []    
       
for x in data['06/04/15']:
    y = x[0]
    z = x[1]
    c = float(carboidratos[y])
    i = float (z)
    r = c*i/100
    carboidratos_06_abril.append(r)
#    print(y,'-',  'carboidratos(g):'  ,r)
    
grafico_c.append(sum(carboidratos_06_abril))
    
    
  


gorduras_06_abril = []
      
for x in data['06/04/15']:
    y = x[0]
    z = x[1]
    c = float(gorduras[y])
    i = float (z)
    r = c*i/100
    gorduras_06_abril.append(r)
#    print(y,'-',  'gorduras(g):'  ,r)
    
grafico_g.append(sum(gorduras_06_abril))


calorias_07_abril = []    
    
for x in data['07/04/15']:
    y = x[0]
    z = x[1]
    c = float(calorias[y])
    i = float (z)
    r = c*i/100
    calorias_07_abril.append(r)
#    print(y,'-',  'calorias(kcal):'  ,r)
    
grafico_kcal.append(sum(calorias_07_abril))


    
proteínas_07_abril = []     
    
for x in data['07/04/15']:
    y = x[0]
    z = x[1]
    c = float(proteínas[y])
    i = float (z)
    r = c*i/100
    proteínas_07_abril.append(r)
#    print(y,'-',  'proteínas(g):'  ,r)
    
grafico_p.append(sum(proteínas_07_abril))
    


carboidratos_07_abril = []     
    
for x in data['07/04/15']:
    y = x[0]
    z = x[1]
    c = float(carboidratos[y])
    i = float (z)
    r = c*i/100
    carboidratos_07_abril.append(r)
#    print(y,'-',  'carboidratos(g):'  ,r)
    
    
grafico_c.append(sum(carboidratos_07_abril))
    


gorduras_07_abril = []   
    
for x in data['07/04/15']:
    y = x[0]
    z = x[1]
    c = float(gorduras[y])
    i = float (z)
    r = c*i/100
    gorduras_07_abril.append(r)
#    print(y,'-',  'gorduras(g):'  ,r)
    
grafico_g.append(sum(gorduras_07_abril))

########## Contas ############################################################



def TMBHomens (peso,altura,idade):
    TMB = 88.36 + (13.4*peso) + (480*altura) - (5.7*idade)
    peso = int(dados[2])
    altura = float(dados[4])
    idade = int(dados[1])
    return TMB
    return peso
    return altura
    return idade
    
#print(TMBHomens(peso,altura,idade))



def TMBMulheres (peso,altura,idade):
    TMB = 447.6 + (9.2*peso) + (310*altura) - (4.3*idade)
    peso = int(dados[2])
    altura = float(dados[4])
    idade = int(dados[1])
    return TMB
    return peso
    return altura
    return idade
    
#print (TMBMulheres(peso,altura,idade)) 
    
    
def IMC (peso,altura):
    IMC = float(( 1.3*peso)/(altura**2.5))
    peso = int(dados[2])
    altura = float(dados[4])
    return IMC
    return peso
    return altura
    
print(IMC(peso,altura))



#if IMC(peso,altura) < 18.5:
#    print('Tá bem frangolino, parça')
#    
#if IMC(peso,altura) >= 18.5 and IMC <= 25:
#    print ('Tá bem saudável')
#    
#if IMC(peso,altura) > 25 and IMC <= 29.9:
#    print ('Tá no sobrepeso, meu')
#    
#if IMC(peso,altura) > 30:
#    print ('Tá toda obesidade, cara')
    
    
    

    
    
dic = {}

dic["minimo"] = 1.2
dic["baixo"] = 1.375
dic['medio'] = 1.55
dic ['alto'] = 1.725
dic ['muito alto'] = 1.9

grafico_recomendadas = []

recomendadas = TMBHomens(peso,altura,idade)*dic['alto']
grafico_recomendadas.append(recomendadas) #06/04/15
grafico_recomendadas.append(recomendadas) #07/04/15   
print (grafico_recomendadas)

##############################################################################








#################### Gráficos ################################################


tempo = range(0,2)

import matplotlib.pyplot as plt

plt.plot(tempo,grafico_kcal)
plt.plot(tempo,grafico_recomendadas)
plt.axis(0,2,0,3000)
plt.xlabel('Datas')
plt.ylabel('Calorias (kcal)')  
plt.title ('Calorias recomendadas e consumidas')
plt.show()

plt.plot(tempo,grafico_p)
plt.axis(0,2,0,40)
plt.xlabel(' Datas' )
plt.ylabel(' Proteínas(g)')  
plt.title ('Proteínas consumidas')
plt.show()

plt.plot(tempo,grafico_c)
plt.axis(0,2,0,250)
plt.xlabel(' Datas' )
plt.ylabel(' Carboidratos(g)')  
plt.title ('Carboidratos consumidos')
plt.show()

plt.plot(tempo,grafico_g)
plt.axis(0,2,0,60)
plt.xlabel(' Datas' )
plt.ylabel(' Gorduras(g)')  
plt.title ('Gorduras consumidas')
plt.show()

print(grafico_kcal)
print(grafico_p)
print(grafico_c)
print(grafico_g)









saida = open ('saida.txt','w')
k = saida.write('Seu índice de massa corporal (IMC) é de 26,41, ou seja, você está no sobrepeso. Suas necessidades calóricas diárias são de 2833.4 kcal, mas você fez um consumo de apenas 462.5 kcal em 06/04/15 e 1091.0 kcal em 07/04/15. Cuidado com essas grandes diminuições !' )
print (k)







