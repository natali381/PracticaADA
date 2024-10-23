import pandas as pd
import matplotlib.pyplot as plt
import os
import numpy as np

def leer_archivo(ruta):
    try:
        df = pd.read_csv(ruta, header=0, encoding='latin-1')
        df.columns = ['tamaño', 'tiempo']
        return df
    except pd.errors.EmptyDataError:
        print(f"Error: El archivo está vacío: {ruta}")
    except pd.errors.ParserError as e:
        print(f"Error de análisis en el archivo {ruta}: {e}")
    except Exception as e:
        print(f"Error inesperado al leer {ruta}: {e}")
    return None

def ajustar_eje_x(plt, df):
    x_ticks = np.arange(len(df['tamaño']))
    x_labels = [f"{size:,}" for size in df['tamaño']]
    plt.xticks(x_ticks, x_labels, rotation=45, ha='right')
    plt.margins(x=0.02)
    plt.subplots_adjust(bottom=0.2)

def crear_grafica_comparacion_dos_lenguajes(algoritmo, lang1, lang2, df1, df2, output_dir):
    plt.style.use('seaborn-v0_8-darkgrid')
    fig = plt.figure(figsize=(15, 10), dpi=300)
    ax = plt.gca()
    
    x1 = np.arange(len(df1['tamaño']))
    
    ax.plot(x1, df1['tiempo'], '-', 
           label=lang1, 
           linewidth=2.5,
           alpha=0.8)
    ax.plot(x1, df2['tiempo'], '-', 
           label=lang2, 
           linewidth=2.5,
           alpha=0.8)
    
    plt.title(f'Comparación de {algoritmo}: {lang1} vs {lang2}',
             fontsize=16, pad=20, fontweight='bold')
    plt.xlabel('Tamaño de entrada', fontsize=12, labelpad=10)
    plt.ylabel('Tiempo (segundos)', fontsize=12, labelpad=10)
    plt.grid(True)
    plt.legend(loc='center left', bbox_to_anchor=(1, 0.5),
              fontsize=10, framealpha=0.9)
    
    ajustar_eje_x(plt, df1)
    
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, f'{algoritmo}_{lang1}_vs_{lang2}.png'),
                bbox_inches='tight', dpi=300)
    plt.close()

def crear_grafica_todos_algoritmos(lenguaje, dataframes, output_dir):
    plt.style.use('seaborn-v0_8-darkgrid')
    
    colores = {
        'bubblesort': '#FF6B6B',    # Rojo coral
        'countingsort': '#4ECDC4',   # Turquesa
        'heapsort': '#45B7D1',       # Azul claro
        'insertionsort': '#96CEB4',  # Verde menta
        'mergesort': '#FFBE0B',      # Amarillo
        'quicksort': '#FF006E',      # Rosa
        'selectionsort': '#8338EC'   # Púrpura
    }
    
    fig = plt.figure(figsize=(15, 10), dpi=300)
    ax = plt.gca()
    
    primer_df = next(iter(dataframes.values()))
    x = np.arange(len(primer_df['tamaño']))
    
    for algoritmo, df in dataframes.items():
        ax.plot(x, df['tiempo'], '-', 
                label=algoritmo.capitalize(),
                color=colores.get(algoritmo.lower()),
                linewidth=2.5,
                alpha=0.8)
    
    plt.title(f'Comparación de Algoritmos de Ordenamiento en {lenguaje}', 
             fontsize=16, pad=20, fontweight='bold')
    plt.xlabel('Tamaño de entrada', fontsize=12, labelpad=10)
    plt.ylabel('Tiempo (segundos)', fontsize=12, labelpad=10)
    plt.grid(True)
    plt.legend(loc='center left', bbox_to_anchor=(1, 0.5),
              fontsize=10, framealpha=0.9)
    
    ajustar_eje_x(plt, primer_df)
    
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, f'todos_algoritmos_{lenguaje}.png'),
                bbox_inches='tight', dpi=300)
    plt.close()

def crear_grafica_tres_lenguajes(algoritmo, df_cpp, df_java, df_python, output_dir):
    plt.style.use('seaborn-v0_8-darkgrid')
    fig = plt.figure(figsize=(15, 10), dpi=300)
    ax = plt.gca()
    
    x = np.arange(len(df_cpp['tamaño']))
    
    estilos = {
        'C++': '-',
        'Java': '--',
        'Python': ':'
    }
    
    ax.plot(x, df_cpp['tiempo'], estilos['C++'],
            label='C++', linewidth=2.5, alpha=0.8)
    ax.plot(x, df_java['tiempo'], estilos['Java'],
            label='Java', linewidth=2.5, alpha=0.8)
    ax.plot(x, df_python['tiempo'], estilos['Python'],
            label='Python', linewidth=2.5, alpha=0.8)
    
    plt.title(f'Comparación de {algoritmo}: C++ vs Java vs Python',
             fontsize=16, pad=20, fontweight='bold')
    plt.xlabel('Tamaño de entrada', fontsize=12, labelpad=10)
    plt.ylabel('Tiempo (segundos)', fontsize=12, labelpad=10)
    plt.grid(True)
    plt.legend(loc='center left', bbox_to_anchor=(1, 0.5),
              fontsize=10, framealpha=0.9)
    
    ajustar_eje_x(plt, df_cpp)
    
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, f'{algoritmo}_tres_lenguajes.png'),
                bbox_inches='tight', dpi=300)
    plt.close()

def main():
    output_dir = 'figuras_comparativas'
    os.makedirs(output_dir, exist_ok=True)

    algoritmos = ['bubblesort', 'countingsort', 'heapsort', 'insertionsort',
                 'mergesort', 'quicksort', 'selectionsort']

    dfs_cpp = {}
    dfs_java = {}
    dfs_python = {}

    for algoritmo in algoritmos:
        dfs_cpp[algoritmo] = leer_archivo(f'resultados_cpp/resultados_{algoritmo}.csv')
        dfs_java[algoritmo] = leer_archivo(f'resultados_java/resultados_{algoritmo}.csv')
        dfs_python[algoritmo] = leer_archivo(f'resultados_python/resultados_{algoritmo}.csv')

    comparaciones = [('C++', 'Python'), ('C++', 'Java'), ('Java', 'Python')]
    for algoritmo in algoritmos:
        for lang1, lang2 in comparaciones:
            df1 = dfs_cpp[algoritmo] if lang1 == 'C++' else (dfs_java[algoritmo] if lang1 == 'Java' else dfs_python[algoritmo])
            df2 = dfs_cpp[algoritmo] if lang2 == 'C++' else (dfs_java[algoritmo] if lang2 == 'Java' else dfs_python[algoritmo])
            crear_grafica_comparacion_dos_lenguajes(algoritmo, lang1, lang2, df1, df2, output_dir)

    crear_grafica_todos_algoritmos('C++', dfs_cpp, output_dir)
    crear_grafica_todos_algoritmos('Java', dfs_java, output_dir)
    crear_grafica_todos_algoritmos('Python', dfs_python, output_dir)

    for algoritmo in algoritmos:
        crear_grafica_tres_lenguajes(
            algoritmo,
            dfs_cpp[algoritmo],
            dfs_java[algoritmo],
            dfs_python[algoritmo],
            output_dir
        )

if __name__ == "__main__":
    main()
    print("¡Todas las gráficas han sido generadas en el directorio 'figuras_comparativas'!")