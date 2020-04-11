#!/usr/bin/env python
#-*- coding: utf-8 -*-

'''
Subrotina necessária para a dinâmica de esferas duras.
autor do programa: Patricia Ternes Dallagnollo
'''

import numpy as np
 
def fcc(Ncelas):
 
  N     = 4 * Ncelas**3
  Runit = np.zeros((4, 3), dtype=np.float)
  R     = np.zeros((N, 3), dtype=np.float)
 
  #tamanho da cela unitaria
  a = 1.0 / Ncelas
 
  #posição das partículas na cela unitária
  Runit[0,0] = 0.0
  Runit[0,1] = 0.0
  Runit[0,2] = 0.0
  Runit[1,0] = 0.0
  Runit[1,1] = 0.5 * a
  Runit[1,2] = 0.5 * a
  Runit[2,0] = 0.5 * a
  Runit[2,1] = 0.0
  Runit[2,2] = 0.5 * a
  Runit[3,0] = 0.5 * a
  Runit[3,1] = 0.5 * a
  Runit[3,2] = 0.0
 
  #coloca todas as partículas
  cont = 0
  for i in xrange(Ncelas):
    for j in xrange(Ncelas):
      for k in xrange(Ncelas):
        for ij in xrange(4):
          if (cont <= N-4):
            R[cont+ij, 0] = Runit[ij,0] + a*k
            R[cont+ij, 1] = Runit[ij,1] + a*j
            R[cont+ij, 2] = Runit[ij,2] + a*i
        cont = cont + 4
  
  #centralizando
  for i in range(N):
    for j in range(3):
        R[i,j] = R[i,j] - 0.5
         
  return R
 
#------------------------------------------------------------
 
def velIni(N, semente, temperatura):

  sigma = np.sqrt(temperatura)
  V     = np.zeros((N, 3), dtype=float)
  vcm   = np.zeros((3), dtype=float)
  conjAleaNum = np.random.RandomState(seed=semente)
  for i in range(3):
    '''atribuição das velocidades'''
    V[:,i]  = conjAleaNum.normal(loc=0.0, scale=sigma, size=N)
    vcm[i] = np.sum(V[:,i])
    vcm[i] = vcm[i] / N
    V[:,i] = V[:,i] - vcm[i]
   
  return V 
