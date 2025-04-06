# Importação das bibliotecas necessárias
import numpy as np  # Usada para operações matemáticas e criação de arrays
import matplotlib.pyplot as plt  # Usada para gerar gráficos
import matplotlib.ticker as ticker  # Ajuda a customizar os marcadores dos eixos

# Função que calcula a aproximação de uma onda quadrada usando Série de Fourier
def serie_de_fourier_onda_quadrada(t, T, N):
    """
    Calcula a série de Fourier truncada para uma onda quadrada.
    t: vetor de tempo
    T: período da onda
    N: número de harmônicos (quanto mais, mais próximo da forma real)
    """
    f = 0
    for k in range(1, 2*N, 2):  # Apenas os termos ímpares: 1, 3, 5, ...
        f += (4 / (k * np.pi)) * np.sin((2 * np.pi * k * (t + 1)) / T)  # Deslocamento de 1 unidade para a esquerda
    return f

# Definindo os parâmetros da onda
T = 4      # Período da onda quadrada (quanto tempo leva um ciclo completo)
N = 60     # Número de harmônicos (define o nível de detalhe na aproximação)

t = np.linspace(-8, 8, 1000)  # Gera 1000 valores igualmente espaçados entre -8 e 8
gx = serie_de_fourier_onda_quadrada(t, T, N)  # Calcula a aproximação da onda quadrada

# Criando o gráfico
plt.figure(figsize=(10, 5))  # Tamanho da imagem: 10 de largura por 5 de altura

# Linha principal da série de Fourier
plt.plot(t, gx, label=f'{N} harmônicos', color='blue', linewidth=2)

# Linhas auxiliares para destacar os níveis superior e inferior da onda
plt.axhline(y=1, color='gray', linestyle='--', linewidth=1, alpha=0.7)
plt.axhline(y=-1, color='gray', linestyle='--', linewidth=1, alpha=0.7)

# Linha vertical no centro do gráfico (tempo = 0)
plt.axvline(x=0, color='black', linestyle=':', linewidth=1)

# Rótulos dos eixos
plt.xlabel('Tempo (t)', fontsize=12)
plt.ylabel('Amplitude x(t)', fontsize=12)

# Título do gráfico
plt.title('Aproximação de Onda Quadrada usando Série de Fourier', fontsize=14, weight='bold')

# Legenda explicando a curva principal
plt.legend(fontsize=10)

# Grade no fundo do gráfico para facilitar a leitura
plt.grid(True, which='both', linestyle='--', linewidth=0.5, alpha=0.7)

# Ajusta os marcadores dos eixos para facilitar a visualização
plt.gca().xaxis.set_major_locator(ticker.MultipleLocator(1))
plt.gca().yaxis.set_major_locator(ticker.MultipleLocator(0.5))

# Garante que nada fique espremido no gráfico
plt.tight_layout()

# Exibe o gráfico
plt.show()