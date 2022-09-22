// Javier Figueroa Estrada
// implementación del selection sort

public void seleccion (int[] arr) {
                        // arreglo llamado arr 
	int i, j, minValue, minIndex, temp = 0; // todos los valores son cero
	for (i = 0; i < arr.length; i++) {
	// las iteraciones deben de ir desde el inicio del arreglo y finalizar con la longitud de este    
		minValue = arr[i]; // inicializamos el primer valor de la listar sin ordenar
		minIndex = i;      // inicializamos el primer índice de la listar sin ordenar
		for (j = i; j < arr.length; j++) {
	// las iteraciones deben de ir desde el primer elemento sin ordenar y finalizar con el último de la lista  
			if (arr[j] < minValue) { // si el valor de j es menor al mínimo
				minValue = arr[j];   // el nuevo valor mínimo es tomado por j
			    minIndex = j;        // el nuevo índice es j
			}
		}
		if (minValue < arr[i]) {// si el valor minimo es el menor al valor en la posición
			temp = arr[i]; // almacenamos el valor en temp par no perder el valor
			arr[i] = arr[minIndex]; // hacemos el cambio de valores en la posición respectiva
			arr[minIndex] = temp;
		}
	}
	return arr;
	
}
  /*  
public static void main(String args[]){
    seleccion lista1 = new seleccion(); 
    lista1 = {64,25,12,22,11}; 
    System.out.println("Array ordenado"); 
    System.out.println(lista1);
    } 
} */ 