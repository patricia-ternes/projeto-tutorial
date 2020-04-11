#!/usr/bin/env python
#-*- coding: utf-8 -*-

'''
Subrotina necessária para a dinâmica de esferas duras.
autor do programa: Patricia Ternes Dallagnollo
'''

import numpy as np
 
def tempo(sigSq, ri, rj, vi, vj):
  tmin  = 1.0e300
  rij = ri - rj
  for i in xrange(3):
    if (rij[i] >= 0.5):
      rij[i] = rij[i] - 1.0
    if (rij[i] <= -0.5):
      rij[i] = rij[i] + 1.0
   
  vij = vi - vj
  bij = np.sum(rij*vij) 
   
  if (bij < 0.0):
    rij2 = np.sum(rij*rij)
    vij2 = np.sum(vij*vij)
    disc = bij**2 - vij2*(rij2 - sigSq)
     
    if (disc > 0.0):
      tempoCol = (-bij - np.sqrt(disc)) / vij2
      if (tempoCol < tmin):
        tmin = tempoCol
         
  return(tmin)
   
#------------------------------------------------------------
 
def tabela(sigSq, R, V):
  N = R.shape[0]
  tabelaColisao    = np.ones(N, dtype=np.float)
  colideCom        = np.zeros(N, dtype=np.int)
  tabelaColisao[:] = 1.0E300
   
  ri = np.zeros(3, dtype=np.float)
  rj = np.zeros(3, dtype=np.float)
  vi = np.zeros(3, dtype=np.float)
  vj = np.zeros(3, dtype=np.float)
   
  for i in range(N-1):
    ri[:] = R[i,:]
    vi[:] = V[i,:]
    for j in range(i+1,N):
      rj[:] = R[j,:]
      vj[:] = V[j,:]
       
      tempCol = tempo(sigSq, ri, rj, vi, vj)
      if (tempCol < tabelaColisao[i]):
        tabelaColisao[i] = tempCol
        colideCom[i]     = j
      if (tempCol < tabelaColisao[j]):
        tabelaColisao[j] = tempCol
        colideCom[j]     = i

  return(colideCom, tabelaColisao)
 
#------------------------------------------------------------
 
def atualizaTabela(sigSq, test_i, test_j, colideCom, tabelaColisao, R, V):
   
  ri = np.zeros(3, dtype=np.float)
  rj = np.zeros(3, dtype=np.float)
  vi = np.zeros(3, dtype=np.float)
  vj = np.zeros(3, dtype=np.float)
   
  N = R.shape[0]
  for i in range(N):
    checa = False
    if (i == test_i or colideCom[i] == test_i):
      checa = True
    if (i == test_j or colideCom[i] == test_j):
      checa = True
   
    if (checa):
      ri[:] = R[i,:]
      vi[:] = V[i,:]
      tabelaColisao[i] = 1.0E300
      for j in range(N):
        if (i != j):
          rj[:] = R[j,:]
          vj[:] = V[j,:]
 
          tempoCol = tempo(sigSq, ri, rj, vi, vj)
          if (tempoCol < tabelaColisao[i]):
            tabelaColisao[i] = tempoCol
            colideCom[i]    = j
          if (tempoCol < tabelaColisao[j]):
            tabelaColisao[j] = tempoCol
            colideCom[j]    = i
  return(colideCom, tabelaColisao)
 
#------------------------------------------------------------
 
def proxCol(colideCom, tabelaColisao):
  tempoCol  = tabelaColisao.min()
  colDaPart = tabelaColisao.argmin()
  
  return (colDaPart, colideCom[colDaPart], tempoCol) 
