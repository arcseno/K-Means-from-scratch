from KMeans import KMeans
import matplotlib.pyplot as plt
import numpy as np

# Conjunto de dados do exemplo: Segmentação de Clientes de Academia.
# Formato: (IMC, Frequência Semanal de Exercícios)

X = np.array([
    [24, 2],
    [27, 3],
    [23, 1],
    [30, 5],
    [22, 2],
    [33, 6],
    [31, 5],
    [29, 4]
])

# -------------------------------------------------- #
# Implementação do Método do Cotovelo (Elbow Method) #
# -------------------------------------------------- #
# Aqui, calcularemos o WCSS (Soma dos Quadrados Intra-Cluster), e faremos o resto abaixo:

def calcular_wcss(X, labels, centroides):
    soma_dos_erros = 0
    for i in range(len(X)):
        ponto = X[i]
        cluster_atual = labels[i]
        centroide_atual = centroides[cluster_atual]
        
        # Calcula a distancia do cliente até o "X" do grupo dele e eleva ao quadrado
        distancia = np.linalg.norm(ponto - centroide_atual)
        soma_dos_erros += distancia ** 2
        
    return soma_dos_erros

# Com a função pronta, começamos a calcular o WCSS para cada valor de K, e depois plotamos o gráfico do método do cotovelo.

valores_wcss = []
k_tentativas = range(1,8)

for k in k_tentativas:
    np.random.seed(42)
    kmeans = KMeans(n_clusters=k, max_iter=300, tol=0.0001)
    labels_cotovelo = kmeans.fit_predict(X)

    erro = calcular_wcss(X, labels_cotovelo, kmeans.centroids)
    valores_wcss.append(erro)

plt.figure()
plt.plot(k_tentativas, valores_wcss, marker='o', color='blue')
plt.title('Elbow Method')
plt.xlabel('Number of Clusters (K)')
plt.ylabel('WCSS (Error)')
plt.savefig('elbow_method.png')
plt.show()

# ----------------------------------------------------------- #
# Gráfico de dispersão com os clusters e os centroides finais #
# ----------------------------------------------------------- #
# Dada a etapa anterior, chegamos na conclusão de que a quantidade ideal para K é 2. Agora, rodamos o modelo.

np.random.seed(42)
kmeans_final = KMeans(n_clusters=2, max_iter=300, tol=0.0001)
labels_finais = kmeans_final.fit_predict(X)
centroides_final = kmeans_final.centroids

plt.figure()
plt.scatter(X[:, 0], X[:, 1], c=labels_finais)
plt.scatter(centroides_final[:, 0], centroides_final[:, 1], c='red', marker='x')
plt.title('Gym Customer Segmentation')
plt.xlabel('BMI')
plt.ylabel('Weekly Frequency')
plt.savefig('kmeans_plot.png')
plt.show()