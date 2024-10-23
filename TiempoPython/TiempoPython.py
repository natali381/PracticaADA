import os
import time
import csv

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def counting_sort(arr):
    max_val = max(arr)
    count = [0] * (max_val + 1)
    
    for num in arr:
        count[num] += 1
    
    index = 0
    for i in range(len(count)):
        while count[i] > 0:
            arr[index] = i
            index += 1
            count[i] -= 1

def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

def selection_sort(arr):
    for i in range(len(arr) - 1):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def main():


    
    current_dir = os.getcwd()
    print(f"Directorio actual: {current_dir}")
    
    data_path = os.path.join(current_dir,"data")
    print(f"Buscando datos en: {data_path}")
    
  
    if not os.path.exists(data_path):
        print("Error: No se encuentra el directorio de datos")
        print(f"Ruta esperada: {data_path}")
        return
    


    
    algoritmos = {
        "bubble_sort": bubble_sort,
        "counting_sort": counting_sort,
        "heap_sort": heap_sort,
        "insertion_sort": insertion_sort,
        "merge_sort": merge_sort,
        "quick_sort": lambda x: quick_sort(x, 0, len(x)-1),
        "selection_sort": selection_sort
    }
    
    archivos = [
        "100.txt", "500.txt", "1000.txt", "2000.txt", "3000.txt",
        "4000.txt", "5000.txt", "6000.txt", "7000.txt", "8000.txt",
        "9000.txt", "10000.txt", "20000.txt", "30000.txt",
        "40000.txt", "50000.txt", "60000.txt", "70000.txt",
        "80000.txt", "90000.txt", "100000.txt"
    ]

    for nombre_algoritmo, funcion in algoritmos.items():
        resultados_path = f"resultados_{nombre_algoritmo}.csv"
        
        with open(resultados_path, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Tamaño", "Tiempo(segundos)"])
            
            for archivo in archivos:
                archivo_path = os.path.join(data_path, archivo)
                try:
                    with open(archivo_path, 'r') as f:
                        numeros = list(map(int, f.readline().strip().split()))
                    
                    array_copy = numeros.copy()
                    tamaño = archivo.replace('.txt', '')
                    
                    inicio = time.time()
                    funcion(array_copy)
                    fin = time.time()
                    
                    tiempo_total = fin - inicio
                    
                    print(f"{nombre_algoritmo} - {tamaño}: {tiempo_total:.6f} segundos")
                    writer.writerow([tamaño, f"{tiempo_total:.6f}"])
                    
                except FileNotFoundError:
                    print(f"Error: No se encontró el archivo {archivo_path}")
                except Exception as e:
                    print(f"Error al procesar {archivo}: {str(e)}")
        
        print(f"\nLos resultados de {nombre_algoritmo} se han guardado en: {resultados_path}")

if __name__ == "__main__":
    main()