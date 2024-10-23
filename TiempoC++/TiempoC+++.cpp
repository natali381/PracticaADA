#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <chrono>
#include <algorithm>
#include <sstream>
#include <iomanip>
#include <filesystem>


class SortingAlgorithms {
private:
    static void heapify(std::vector<int>& arr, int n, int i) {
        int largest = i;
        int left = 2 * i + 1;
        int right = 2 * i + 2;

        if (left < n && arr[left] > arr[largest])
            largest = left;

        if (right < n && arr[right] > arr[largest])
            largest = right;

        if (largest != i) {
            std::swap(arr[i], arr[largest]);
            heapify(arr, n, largest);
        }
    }

    static int partition(std::vector<int>& arr, int low, int high) {
        int pivot = arr[high];
        int i = low - 1;

        for (int j = low; j < high; j++) {
            if (arr[j] <= pivot) {
                i++;
                std::swap(arr[i], arr[j]);
            }
        }
        std::swap(arr[i + 1], arr[high]);
        return i + 1;
    }

public:
    static void bubbleSort(std::vector<int>& arr) {
        int n = arr.size();
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n - i - 1; j++) {
                if (arr[j] > arr[j + 1]) {
                    std::swap(arr[j], arr[j + 1]);
                }
            }
        }
    }

    static void countingSort(std::vector<int>& arr) {
        int maxVal = *std::max_element(arr.begin(), arr.end());
        std::vector<int> count(maxVal + 1, 0);
        
        for (int num : arr) {
            count[num]++;
        }

        int index = 0;
        for (int i = 0; i <= maxVal; i++) {
            while (count[i] > 0) {
                arr[index] = i;
                index++;
                count[i]--;
            }
        }
    }

    static void heapSort(std::vector<int>& arr) {
        int n = arr.size();

        for (int i = n / 2 - 1; i >= 0; i--)
            heapify(arr, n, i);

        for (int i = n - 1; i > 0; i--) {
            std::swap(arr[0], arr[i]);
            heapify(arr, i, 0);
        }
    }

    static void insertionSort(std::vector<int>& arr) {
        for (int j = 1; j < arr.size(); j++) {
            int actual = arr[j];
            int i = j - 1;
            while (i >= 0 && arr[i] > actual) {
                arr[i + 1] = arr[i];
                i--;
            }
            arr[i + 1] = actual;
        }
    }

    static void mergeSort(std::vector<int>& arr) {
        if (arr.size() <= 1) return;

        int mid = arr.size() / 2;
        std::vector<int> left(arr.begin(), arr.begin() + mid);
        std::vector<int> right(arr.begin() + mid, arr.end());

        mergeSort(left);
        mergeSort(right);

        std::merge(left.begin(), left.end(),
                  right.begin(), right.end(),
                  arr.begin());
    }

    static void quickSort(std::vector<int>& arr, int low, int high) {
        if (low < high) {
            int pi = partition(arr, low, high);
            quickSort(arr, low, pi - 1);
            quickSort(arr, pi + 1, high);
        }
    }

    static void selectionSort(std::vector<int>& arr) {
        for (int i = 0; i < arr.size() - 1; i++) {
            int minIdx = i;
            for (int j = i + 1; j < arr.size(); j++) {
                if (arr[j] < arr[minIdx]) {
                    minIdx = j;
                }
            }
            if (minIdx != i) {
                std::swap(arr[i], arr[minIdx]);
            }
        }
    }
};

std::vector<int> readArrayFromFile(const std::string& filename) {
    std::vector<int> numbers;
    std::ifstream file(filename);
    std::string line;
    
    if (file.is_open()) {
        if (getline(file, line)) {
            std::istringstream iss(line);
            int number;
            while (iss >> number) {
                numbers.push_back(number);
            }
        }
        file.close();
    } else {
        std::cerr << "No se pudo abrir el archivo: " << filename << std::endl;
    }
    
    return numbers;
}



int main() {
    // Usa barras normales o dobles barras invertidas para la ruta
    std::string dataPath = "D:/analisissssss/Analisis222/TiempoC++/data/";
    // Alternativa: std::string dataPath = "D:\\analisissssss\\Analisis222\\TiempoC++\\data\\";
    
    
   
    
    std::vector<std::string> algoritmos = {
        "BubbleSort", "CountingSort", "HeapSort", "InsertionSort",
        "MergeSort", "QuickSort", "SelectionSort"
    };

    std::vector<std::string> archivos = {
        "100.txt", "500.txt", "1000.txt", "2000.txt", "3000.txt",
        "4000.txt", "5000.txt", "6000.txt", "7000.txt", "8000.txt",
        "9000.txt", "10000.txt", "20000.txt", "30000.txt",
        "40000.txt", "50000.txt", "60000.txt", "70000.txt",
        "80000.txt", "90000.txt", "100000.txt"
    };

    for (const auto& algoritmo : algoritmos) {
        std::string resultadosPath = dataPath + "resultados_" + algoritmo + ".csv";
        std::ofstream resultFile(resultadosPath);
        
        if (!resultFile.is_open()) {
            std::cerr << "Error: No se pudo crear el archivo: " << resultadosPath << std::endl;
            continue;
        }
        
        resultFile << "Tamano,Tiempo(segundos)\n";  // Removed ñ to avoid encoding issues
        std::cout << "\nProcesando " << algoritmo << "...\n";

        for (const auto& archivo : archivos) {
            std::string fullPath = dataPath + archivo;
            auto arr = readArrayFromFile(fullPath);
            
            if (arr.empty()) {
                std::cerr << "Error: No se pudo leer el archivo " << fullPath << std::endl;
                continue;
            }

            auto start = std::chrono::high_resolution_clock::now();

            if (algoritmo == "BubbleSort")
                SortingAlgorithms::bubbleSort(arr);
            else if (algoritmo == "CountingSort")
                SortingAlgorithms::countingSort(arr);
            else if (algoritmo == "HeapSort")
                SortingAlgorithms::heapSort(arr);
            else if (algoritmo == "InsertionSort")
                SortingAlgorithms::insertionSort(arr);
            else if (algoritmo == "MergeSort")
                SortingAlgorithms::mergeSort(arr);
            else if (algoritmo == "QuickSort")
                SortingAlgorithms::quickSort(arr, 0, arr.size() - 1);
            else if (algoritmo == "SelectionSort")
                SortingAlgorithms::selectionSort(arr);

            auto end = std::chrono::high_resolution_clock::now();
            std::chrono::duration<double> diff = end - start;

            std::string size = archivo.substr(0, archivo.find(".txt"));
            
            std::cout << algoritmo << " - " << size << ": " 
                     << std::fixed << std::setprecision(6) << diff.count() 
                     << " segundos" << std::endl;
            
            resultFile << size << "," 
                      << std::fixed << std::setprecision(6) << diff.count() << "\n";
        }

        resultFile.close();
        std::cout << "Resultados guardados en: " << resultadosPath << std::endl;
    }

    return 0;
}