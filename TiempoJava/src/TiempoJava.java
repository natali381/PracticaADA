/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */


import javax.swing.*;
import java.io.*;
import java.util.Arrays;

/**
 *
 * @author ADMIN
 */
public class TiempoJava {

      public static void bubbleSort(int[] arr) {
        int n = arr.length;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n - i - 1; j++) {
                if (arr[j] > arr[j + 1]) {
                    int temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;
                }
            }
        }
    }

    public static void countingSort(int[] arr) {
        int maxVal = Integer.MIN_VALUE;
        for (int num : arr) {
            if (num > maxVal) {
                maxVal = num;
            }
        }
        
        int[] count = new int[maxVal + 1];
        for (int num : arr) {
            count[num]++;
        }

        int index = 0;
        for (int i = 0; i < count.length; i++) {
            while (count[i] > 0) {
                arr[index] = i;
                index++;
                count[i]--;
            }
        }
    }

    private static void heapify(int[] arr, int n, int i) {
        int largest = i;
        int left = 2 * i + 1;
        int right = 2 * i + 2;

        if (left < n && arr[left] > arr[largest]) {
            largest = left;
        }

        if (right < n && arr[right] > arr[largest]) {
            largest = right;
        }

        if (largest != i) {
            int temp = arr[i];
            arr[i] = arr[largest];
            arr[largest] = temp;
            heapify(arr, n, largest);
        }
    }

    public static void heapSort(int[] arr) {
        int n = arr.length;

        for (int i = n / 2 - 1; i >= 0; i--) {
            heapify(arr, n, i);
        }

        for (int i = n - 1; i > 0; i--) {
            int temp = arr[0];
            arr[0] = arr[i];
            arr[i] = temp;
            heapify(arr, i, 0);
        }
    }

    public static void insertionSort(int[] arr) {
        for (int j = 1; j < arr.length; j++) {
            int actual = arr[j];
            int i = j - 1;
            while (i >= 0 && arr[i] > actual) {
                arr[i + 1] = arr[i];
                i--;
            }
            arr[i + 1] = actual;
        }
    }

    public static void mergeSort(int[] arr) {
        if (arr.length > 1) {
            int mid = arr.length / 2;
            int[] leftHalf = new int[mid];
            int[] rightHalf = new int[arr.length - mid];

            System.arraycopy(arr, 0, leftHalf, 0, mid);
            System.arraycopy(arr, mid, rightHalf, 0, arr.length - mid);

            mergeSort(leftHalf);
            mergeSort(rightHalf);

            int i = 0, j = 0, k = 0;

            while (i < leftHalf.length && j < rightHalf.length) {
                if (leftHalf[i] < rightHalf[j]) {
                    arr[k++] = leftHalf[i++];
                } else {
                    arr[k++] = rightHalf[j++];
                }
            }

            while (i < leftHalf.length) {
                arr[k++] = leftHalf[i++];
            }

            while (j < rightHalf.length) {
                arr[k++] = rightHalf[j++];
            }
        }
    }

    public static void quickSort(int[] arr, int low, int high) {
        if (low < high) {
            int pi = partition(arr, low, high);
            quickSort(arr, low, pi - 1);
            quickSort(arr, pi + 1, high);
        }
    }

    private static int partition(int[] arr, int low, int high) {
        int pivot = arr[high];
        int i = low - 1;
        
        for (int j = low; j < high; j++) {
            if (arr[j] <= pivot) {
                i++;
                int temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }
        
        int temp = arr[i + 1];
        arr[i + 1] = arr[high];
        arr[high] = temp;
        
        return i + 1;
    }

    public static void selectionSort(int[] arr) {
        for (int i = 0; i < arr.length - 1; i++) {
            int minIdx = i;
            for (int j = i + 1; j < arr.length; j++) {
                if (arr[j] < arr[minIdx]) {
                    minIdx = j;
                }
            }
            int temp = arr[minIdx];
            arr[minIdx] = arr[i];
            arr[i] = temp;
        }
    }

    public static void main(String[] args) {
        String dataPath = "src/data/";
        File directory = new File(dataPath);
        
        // Array con los nombres de los algoritmos
        String[] algoritmos = {
            "BubbleSort", "CountingSort", "HeapSort", "InsertionSort",
            "MergeSort", "QuickSort", "SelectionSort"
        };
        
        // Crear archivos para guardar resultados de cada algoritmo
        for (String algoritmo : algoritmos) {
            String resultadosPath = "src/data/resultados_" + algoritmo.toLowerCase()+".csv";
            
            try (FileWriter fw = new FileWriter(resultadosPath);
                 BufferedWriter bw = new BufferedWriter(fw)) {
                
                // Escribir encabezados del CSV
                bw.write("Tamaño,Tiempo(segundos)\n");
                
                String[] archivos = {
                    "100.txt", "500.txt", "1000.txt", "2000.txt", "3000.txt", 
                    "4000.txt", "5000.txt", "6000.txt", "7000.txt", "8000.txt", 
                    "9000.txt", "10000.txt", "20000.txt", "30000.txt", 
                    "40000.txt", "50000.txt", "60000.txt", "70000.txt", 
                    "80000.txt", "90000.txt", "100000.txt"
                };

                for (String archivo : archivos) {
                    File file = new File(directory, archivo);
                    try (BufferedReader br = new BufferedReader(new FileReader(file))) {
                        String line = br.readLine();
                        String[] numsStr = line.split(" ");
                        int[] array = Arrays.stream(numsStr).mapToInt(Integer::parseInt).toArray();
                        int[] arrayCopy = array.clone(); // Crear una copia para cada prueba
                        
                        String tamaño = archivo.replace(".txt", "");
                        
                        long startTime = System.currentTimeMillis();
                        
                        // Ejecutar el algoritmo correspondiente
                        switch (algoritmo) {
                            case "BubbleSort":
                                bubbleSort(arrayCopy);
                                break;
                            case "CountingSort":
                                countingSort(arrayCopy);
                                break;
                            case "HeapSort":
                                heapSort(arrayCopy);
                                break;
                            case "InsertionSort":
                                insertionSort(arrayCopy);
                                break;
                            case "MergeSort":
                                mergeSort(arrayCopy);
                                break;
                            case "QuickSort":
                                quickSort(arrayCopy, 0, arrayCopy.length - 1);
                                break;
                            case "SelectionSort":
                                selectionSort(arrayCopy);
                                break;
                        }
                        
                        long endTime = System.currentTimeMillis();
                        double totalTimeInSeconds = (endTime - startTime) / 1000.0;
                        
                        // Imprimir en consola
                        System.out.printf("%s - %s: %.6f segundos%n", 
                                        algoritmo, tamaño, totalTimeInSeconds);
                        
                        // Guardar en el archivo CSV
                        bw.write(String.format("%s,%.6f\n", tamaño, totalTimeInSeconds));
                        
                    } catch (IOException e) {
                        System.err.println("Error al leer el archivo " + file.getName() + 
                                         ": " + e.getMessage());
                    }
                }
                System.out.println("\nLos resultados de " + algoritmo + 
                                 " se han guardado en: " + resultadosPath);
                
            } catch (IOException e) {
                System.err.println("Error al escribir el archivo de resultados para " + 
                                 algoritmo + ": " + e.getMessage());
            }
        }
    }

}
