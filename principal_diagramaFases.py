#!/usr/bin/env python
#-*- coding: utf-8 -*-
 
'''
Código que descreve o movimento de esferas duras dentro de um cubo de fronteiras periódicas.
A partir dessa dinâmica foi gerado o gráfico do diagrama de fases.
autor do programa: Patricia Ternes Dallagnollo
'''

import numpy as np
import matplotlib.pyplot as plt
import confInicial as inicial
import colisao, dinamica
 
 
Ncelas  = 3
N       = 4 * Ncelas**3
temp    = 0.5
semente = 39284
nColEq  = 200
dt       = 0.1
tempEq   = 5
 
ri = np.zeros(3, dtype=np.float)
rj = np.zeros(3, dtype=np.float)
vi = np.zeros(3, dtype=np.float)
vj = np.zeros(3, dtype=np.float)
 
nome = 'diagramaFases.dat'
arq = open(nome, 'w')

for l in range(1, 65, 1):
  
  eta  = l * 0.01
  rho     = 6.0 * eta / np.pi
  L       = (float(N) / rho)**(1.0/3.0)
  sigma   = 1.0 / L
  sigSq   = sigma*sigma

  R = inicial.fcc(Ncelas)   #posicao atual dos agentes
  N = R.shape[0]            #retorna o numero de agentes, pq nesse programa eh variavel. Mas em outros, esse passo n eh necessario
  V  = inicial.velIni(N, semente, temp)
  
  V2      = V*V
  modV2   = np.sum(V2, axis=1)
  ecinSum = np.sum(modV2)
  
  colideCom, tabelaColisao = colisao.tabela(sigSq, R, V)
  
  soma = 0.0 
  tempoTot = 0.0
  continua = True
  
  while (continua):
    i, j, temProxCol = colisao.proxCol(colideCom, tabelaColisao)
    tempoTot = tempoTot + temProxCol
    
    ri[:] = R[i,:]; rj[:] = R[j,:]
    vi[:] = V[i,:]; vj[:] = V[j,:]
    
    deltaV = vj[:] - vi[:]
    deltaV2 = deltaV*deltaV
    modDeltaV = np.sqrt(sum(deltaV2))
    soma = soma + modDeltaV
    
    tabelaColisao, R = dinamica.movePos(temProxCol, tabelaColisao, R, V)
    ecinSum, V[i,:], V[j,:] = dinamica.modifVel(ecinSum, sigSq, ri, rj, vi, vj)
    colideCom, tabelaColisao = colisao.atualizaTabela(sigSq, i, j, colideCom, tabelaColisao, R, V)
    
    #print tempoTot, temProxCol
    if (tempoTot >= tempEq):
      continua = False
      
  soma = soma * sigma / (ecinSum * tempoTot)	#Tirei o 2, porque simplifiquei com o dois da energia cinética: Ecim = 1/2 * sum(v**2) e 
  z = 1.0 + soma				#no meu programa: ecimsum = sum(v**2).
  print >> arq, eta, z
  
arq.close()
