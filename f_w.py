## -*- coding: utf-8 -*-
##
## @author JavierVM
## @mail javier.vargas.mtz@gmail.com
## @description implementacion floyd_warshal
## @filename f_w.py
## 
## A partir de una matriz de distancias
## calcula la ruta mas corta de todos los
## pares de vertices con el algoritmo
## floyd-warshall
##
#################################################
import numpy as np

ejemplo = np.zeros((4, 4))
tarea = np.zeros((5, 5))
inf = np.inf
ejemplo = [
			[inf,  -1, inf, inf],
			[inf, inf,   3,   7],
			[  5, inf, inf, inf],
			[inf, inf,  -2, inf],
		  ]
tarea = [
			[inf, inf,  -2,  -8, inf],
			[  4, inf,   5,   2,   5],
			[inf, inf,  -1, inf,  -2],
			[inf, inf,   2, inf,   4],
			[  8, inf, inf, inf, inf]
		]
tarea2 = [
			[inf,   1, inf,   1, inf],
			[inf, inf, inf, inf, inf],
			[  3,   6, inf, inf, inf],
			[inf, inf, inf, inf,   1],
			[ -1, inf, inf, inf, inf]
		 ]

# floyd warshall 
def fl_wa(dist):
	print "\t it\ti \tj \tk \td_ij \td_jk \td_ik \tcambio"
	iter = 0
	min = 0
	n = len(dist)
	for j in range(n):
		for i in range(n):
			for k in range(n):			
				if (i != j) and (j != k):
					iter += 1
					min = 0
					print '\t', iter, '\t', i+1, '\t', j+1, '\t', k+1,
					print '\t', dist[i][j], '\t', dist[j][k],
					print '\t', dist[i][k], 
					if ( ( dist[i][j] + dist[j][k] ) < dist[i][k] ):
						dist[i][k] = dist[i][j] + dist [j][k]
						min = 1
					print '\t', min
			if (i == j):
				if (dist[i][j] < 0):
					print "Se ha encontrado un ciclo negativo"
					return 



def printMat(mat):
	n = len(mat)
	for row in range(n):
		print '[',
		for col in range(n):
			print '\t', mat[row][col],
		print ']'


if __name__ == "__main__":
	fl_wa(tarea)
	printMat(tarea)
