# Importação das bibliotecas necessárias
import numpy as np  # Biblioteca para operações numéricas
import matplotlib.pyplot as plt  # Biblioteca para geração de gráficos
import matplotlib.ticker as ticker  # Módulo para ajustar marcações no gráfico
from matplotlib.ticker import FuncFormatter  # Formata os valores dos eixos

# Função que calcula a aproximação de uma onda dente de serra utilizando Série de Fourier
def serie_fourier_onda_dente_de_serra(tempo, periodo, harmonicos):
    """
    Calcula uma aproximação de uma onda dente de serra usando Série de Fourier.

    Parâmetros:
    tempo: vetor com os valores de tempo (em radianos)
    periodo: período da onda dente de serra (em radianos)
    harmonicos: número de harmônicos considerados na aproximação

    Retorna:
    Um array com os valores da onda aproximada.
    """
    resultado = 0
    for k in range(1, harmonicos + 1):
        termo = (-1)**(k+1) * (2 / (k * np.pi)) * np.sin((2 * np.pi * k * tempo) / periodo)
        resultado += termo
    return resultado

# Parâmetros da onda
periodo = 2 * np.pi  # Um ciclo completo da onda ocorre em 2π radianos
harmonicos = 60  # Número de harmônicos usados na série (mais = maior precisão)

# Vetor de tempo variando de -4π a 4π
tempo = np.linspace(-4 * np.pi, 4 * np.pi, 1000)

# Deslocamento de π para alinhar o mínimo em 0 e o máximo em 2π
onda_dente_serra = serie_fourier_onda_dente_de_serra(tempo - np.pi, periodo, harmonicos)

# Função auxiliar para formatar os valores do eixo X como múltiplos de π
def formatar_em_pi(valor, posicao):
    n = int(np.round(valor / np.pi))
    if n == 0:
        return "0"
    elif n == 1:
        return "π"
    elif n == -1:
        return "-π"
    else:
        return f"{n}π"

# Criação do gráfico
plt.figure(figsize=(10, 4))  # Define o tamanho da figura

# Plota a onda calculada
plt.plot(tempo, onda_dente_serra, label='Onda Dente de Serra ajustada', color='red', linewidth=2)

# Linhas de referência para facilitar a leitura
plt.axhline(y=1, color='gray', linestyle='--', linewidth=1, alpha=0.7)
plt.axhline(y=-1, color='gray', linestyle='--', linewidth=1, alpha=0.7)
plt.axvline(x=0, color='black', linestyle=':', linewidth=1)

# Títulos e legendas
plt.xlabel('Tempo (rad)', fontsize=12)
plt.ylabel('Amplitude x(t)', fontsize=12)
plt.title('Onda Dente de Serra', fontsize=14, weight='bold')
plt.legend(fontsize=10)

# Personalização dos eixos
plt.grid(True, which='both', linestyle='--', linewidth=0.5, alpha=0.7)
plt.gca().xaxis.set_major_locator(ticker.MultipleLocator(base=np.pi))
plt.gca().xaxis.set_major_formatter(FuncFormatter(formatar_em_pi))
plt.gca().yaxis.set_major_locator(ticker.MultipleLocator(0.5))

# Ajuste final e exibição
plt.tight_layout()
plt.show()
