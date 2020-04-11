#!/usr/bin/env python
#-*- coding: utf-8 -*-

'''
Subrotina necessária para a dinâmica de esferas duras.
autor do programa: Patricia Ternes Dallagnollo
'''

import numpy as np
import sys
 
def movePos(T, tabelaColisao, R, V):
  tabelaColisao = tabelaColisao - T
   
  teste         = tabelaColisao < 0.0
  if (np.any(teste)):
    sys.exit('Tempo de colisao negativo')   
   
  R  = R + V*T
 
  #condicoes periodicas
  for i in xrange(R.shape[0]):
    for j in xrange(3):
      if (R[i,j] >= 0.5):
        R[i,j] = R[i,j] - 1.0
      if (R[i,j] <= -0.5):
        R[i,j] = R[i,j] + 1.0
   
  return(tabelaColisao, R)
   
#------------------------------------------------------------
   
def modifVel(eCin, sigSq, ri, rj, vi, vj):
   
  dr = ri - rj
   
  for i in xrange(3):
    if (dr[i] >= 0.5):
      dr[i] = dr[i] - 1.0
    if (dr[i] <= -0.5):
      dr[i] = dr[i] + 1.0
       
  dv  = vi - vj
   
  ddv = dr * ( np.sum(dr*dv) / np.sum(dr*dr) )
   
  eCin = eCin - sum(vi*vi) - sum(vj*vj)
 
  vi = vi - ddv
  vj = vj + ddv
   
  eCin = eCin + sum(vi*vi) + sum(vj*vj)
   
  return(eCin, vi, vj) 
