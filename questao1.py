# -*- coding: utf-8 -*-
"""
Created on Sat May  4 16:58:44 2019

@author: _-Douglas-_
"""
import time


#Abre o arquivo com os dados
grafosFile = open("entrada-dos-grafos.txt", "r")
#grafosFile = open("teste1.txt", "r")

#copia dados do arquivo para um lista e fecha o arquivo
grafosList = grafosFile.readlines()
grafosFile.close

#Define a posição atual do arquivo
linhaAtual = 0

#Coleta a Linha Atual e passa para proxima
nVerticesGrafo = int(grafosList[linhaAtual])
linhaAtual = 1

#define o nome do grafo
grafoAtual = 1

#Armazena numero de vertices
numeroVertces = 0

#Armazena numero de arestas
numeroArestas = 0

#Armazena sequencia de grau
sequenciaDeGrau = []

#Armazena lista de vertices
listaVertices = []

#Armazena lista de arestas de cada grafo
listaArestas = []

#String de saida
saida = ""

#Escolha de representação 0 matriz, 1 vetor

representacao=int(input("Escolha de representação de adjacencia 0 matriz, 1 vetor: "))

#Registra horario de incio do script
horaInicio = time.time()

#Matriz de adjacencia
matrizAdjacencia = []

#Vetor de adjacencia
vetorAdjacencia = []

#Laço para percorrer linha a linha
#for linha in range(linhaAtual, nVerticesGrafo):
for linha in range(0, len(grafosList)):
    dadoAtual=grafosList[linha]


    #Valida se é o primeiro grafo encontrado
    if grafoAtual == 1:
        

        #Entra quando inicia um novo    
        if (" " in dadoAtual) == False:
            #pega numero de vertices do grafo atual
            numeroVertces=dadoAtual
        
            #Exibe numero do grafo
#            print("Grafo: " + str(grafoAtual))
            saida = saida+"Grafo: " + str(grafoAtual)
            
            #Atualiza numero do grafo caso tenha mais de um por arquivo
            grafoAtual = grafoAtual+1
            
            #Exibe numero de vertices 
#            print("Número de vértices: " + str(int(dadoAtual)))            
            saida = saida+"\n"+"Número de vértices: " + str(int(dadoAtual))
            

    else:
        
        #Entra quando está no mesmo grafo    
        if (" " in dadoAtual) == False:
            #pega numero de vertices do grafo atual
            numeroVertces=dadoAtual
            
            #Exibe numero de arestas do grafo anterior
#            print("Número de arestas: " + str(numeroArestas))
            saida = saida+"\n"+"Número de arestas: " + str(numeroArestas)
            
            #Ordena lista de vertices
            listaVerticesSort = sorted(listaVertices)
            listaVertices=listaVerticesSort
            
            #calcular sequencia de grau
            for vertice in range(0, len(listaVertices)):
                sequenciaDeGrau.append(listaArestas.count(listaVertices[vertice]))
    
            #exibe sequencia de grau do grafo anterior
#            print("Sequencia de grau: " + str(sorted(sequenciaDeGrau)))
            saida = saida+"\n"+"Sequencia de grau: " + str(sorted(sequenciaDeGrau))
            
            
            #Exibe as vertices
#            print("Vertices: " + str(listaVertices))

            
            #Exibe numero do grafo
#            print("Grafo: " + str(int(grafoAtual)))
            saida = saida+"\n"+"Grafo: " + str(int(grafoAtual))
            
            #Reinicia contagem das arestas
            numeroArestas = 0
            
            #reinicia lista de vertices
            listaVertices = []
            
            #reinicia lista de arestas
            listaArestas = []

            #reinicia sequencia de grau
            sequenciaDeGrau = []
            
            #reinicia matriz de adjacencia
            matrizAdjacencia = []
            
            #reinicia vetor de adjacencia
            vetorAdjacencia = []
            
            
            
            #Exibe numero de vertices 
#            print("Número de vértices: " + str(int(numeroVertces)))  
            saida = saida+"\n"+"Número de vértices: " + str(int(numeroVertces))
            
        else:
            #incrementa numero de arestas
            numeroArestas = numeroArestas+1
            
            #Trata os vertices da aresta
            aresta = dadoAtual.split()

            for linhaVert in range(0, len(aresta)):
                
                #atualiza lista de arestas
                listaArestas.append(aresta[linhaVert])
                
                if (aresta[linhaVert] in listaVertices) == False:
                    listaVertices.append(aresta[linhaVert])
                    


#Exibe numero de arestas do ultimo grafo
#print("Número de arestas: " + str(numeroArestas))
saida = saida+"\n"+"Número de arestas: " + str(numeroArestas)

#Ordena lista de vertices
listaVerticesSort = sorted(listaVertices)
listaVertices=listaVerticesSort

#Exibe as vertices
#print("Vertices: " + str(listaVertices))

#calcular sequencia de grau
for vertice in range(0, len(listaVertices)):
    sequenciaDeGrau.append(listaArestas.count(listaVertices[vertice]))
   
#exibe sequencia de grau do grafo anterior
#print("Sequencia de grau: " + str(sorted(sequenciaDeGrau)))
saida = saida+"\n"+"Sequencia de grau: " + str(sorted(sequenciaDeGrau))


if representacao == 0:
    #Gerar matriz de adjacencia
    #Inicializando matriz
    for linha in range(0, len(listaVertices)+1):
        line = []
        for coluna in range(0, len(listaVertices)+1):
            valor = 0
            line.append(valor)
        matrizAdjacencia.append(line)
        
    #inicializando linha
    for vertice in range(0, len(listaVertices)):
        matrizAdjacencia[0][vertice+1]=int(listaVertices[vertice])
    
    #inicializando coluna
    for vertice in range(0, len(listaVertices)):
        matrizAdjacencia[vertice+1][0]=int(listaVertices[vertice])
    
    #Colocar a adjacencia de cada vertice
    i = 0 
    fim =  len(listaArestas)   
    while i < fim:
        indexOrigem = matrizAdjacencia[0].index(int(listaArestas[i]))
        indexDestino = matrizAdjacencia[0].index(int(listaArestas[i+1]))
        matrizAdjacencia[indexOrigem][indexDestino]= matrizAdjacencia[indexOrigem][indexDestino]+1
        matrizAdjacencia[indexDestino][indexOrigem]= matrizAdjacencia[indexDestino][indexOrigem]+1
        i = i+2

    #exibe matriz de adjacencia
    saida = saida+"\n"+"Matriz: de adjacencia: "
    for linha in range(0, len(matrizAdjacencia)):
#        print(matrizAdjacencia[linha])
        saida = saida+"\n"+str(matrizAdjacencia[linha])

else:
    #Exibe vetor de adjacencia
    i = 0 
    fim =  len(listaArestas)   
    while i < fim:
        indexOrigem = int(listaArestas[i])
        indexDestino = int(listaArestas[i+1])
        vetorAdjacencia.append(str(indexOrigem)+","+str(indexDestino))    
        i = i+2

#    print("Vetor de adjacencia: "+str(vetorAdjacencia))
    saida = saida+"\n"+"Vetor de adjacencia: "+str(vetorAdjacencia)

#Registra horario de termino da execução
horaFim = time.time()

#exibe tempo decorrido total
#print("Tempo de execução: " + str(round(horaFim - horaInicio,4)) + " segundos")
saida = saida+"\n"+"Tempo de execução: " + str(round(horaFim - horaInicio,6)) + " segundos"

#Gera arquivo de saida com as informaçoes
saidaFile = open("saida.txt", "w+")
saidaFile.write(str(saida))
print("Nome do arquivo: " + saidaFile.name)
saidaFile.close



print(saida)
















