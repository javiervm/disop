/* ##
 * ## @author JavierVM
 * ## @mail javier.vargas.mtz@gmail.com
 * ## @description implementacion floyd_warshal
 * ## @filename f_w.cpp
 * ## 
 * ## A partir de una matriz de distancias
 * ## calcula la ruta mas corta de todos los
 * ## pares de vertices con el algoritmo
 * ## floyd-warshall
 * ##
 * ################################################# *
 * */

#include <stdio.h>
#include <iostream>
#include <fstream>
#include <string>
using namespace std;



int main(int argc, char** argv){
	int iter = 0;
	bool min = false;
	int len = 0;

	float dist*;
	string line;
	iftream data("dist.dat");
	if (data.is_open()){
		cout << "Haciendo lectura del archivo..." << endl;
		cout << "Almacenando matriz de distamcias" << endl;
		while(getline(data, line)){
			cout << line << endl;
			//missing atoi for each line and split by coma
		}
	}else{
		cout << "No existe el archivo: \'dist.dat\'" << endl;
	}
	//Algoritmo de floyd warshall dada una matriz de distancias
	for(int j=0; j<len; j++){
		for (int i=0; i<len; i++){
			for (int k=0; k<len; k++){
				if ( i != j ) && ( j != k ){
					iter++;
					cout << '\t' << iter << i+1 << '\t' << j+1 << '\t' << k+1;
					cout << '\t' << dist[i][j] << '\t' << dist[j][k];
					cout << '\t' << dist[i][k];
					if ( ( dist[i][j] + dist[j][k] ) < dist[i][k] ){
						dist[i][k] = dist[i][j] + dist[j][k];
						min = true;
					}
					cout << '\t' << min << endl;			
				}
			}
			if ( i == j ){
				if ( dist[i][j] < 0 ){
					cout << "Se encontro un ciclo negativo" << endl;
					cerr << "Saliendo del programa..." << endl;
					return 0;
				}
			}
		}
	}
	// imporime matriz si termino con exito floyd warshall
	for (int row=0; row < len; row++){
		cout << '['
		for (int col=0; col < len; col++){
			cout << '\t' << dist[row][col];
		}
		cout << ']' << endl;
	}
	return 1;




}
