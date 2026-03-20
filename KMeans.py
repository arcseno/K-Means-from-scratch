'''
[Ex2] Algoritmo K-Means - Aprendizado de Máquina Não Supervisionado - Profº
Gustavo Taiji Naozuka

---------------------------------------------------------------------------

** PLANNING **

1º STEP:

-> O Método fit_predict(x) deve implementar o agrupamento de dados com o
K-Means. Como fazer isso?

    * Deve realizar a inicialização aleatória, escolhendo K pontos (baseado no n_clusters) do conjunto de dados X para serem os centroides iniciais. Aqui dá pra utilizar o random choice do numpy. (FEITO)

    * Depois, para cada ponto do conjunto de dados X, nós calculamos a distância euclidiana em relação a cada um dos K centroides. (FEITO)
    Assim, atribui o ponto ao centroide mais proximo. 

    * Logo após, para cada grupo criado na etapa anterior, calcular a média aritmética das coordenadas de todos os pontos que pertencem a ele. E, finalmente, mover o centroide desse grupo para a nova posição média desse cálculo. (FEITO)

    * O critério de parada, a dita convergência, acontecerá quando:
        -> Os centroides pararam de se mover (a diferença entre a posição antiga e a nova é < que a tolerância dada)
        -> O número máximo de repetições max_iter for atingido.
        (CONFERIDO).

2º STEP:

-> Testar a classe implementada no conjunto de dados do exemplo: Segmentação
de Clientes de Academia.

3º STEP:

-> Fazer um gráfico de dispersão, em que cada ponto é colorido de acordo com o
cluster encontrado, e devem ter os centroides finais (após convergir) com um 
símbolo diferente.

---------------------------------------------------------------------------

'''

import numpy as np

class KMeans:
    def __init__(self, n_clusters=2, max_iter=300, tol=0.0001):
        self.n_clusters = n_clusters
        self.max_iter = max_iter
        self.tol = tol
        self.centroids = None

    def fit_predict(self, X):
        # Sorteia, inicialmente, os centroides iniciais
        indices_aleatorios = np.random.choice(len(X), self.n_clusters, replace=False)
        self.centroids = X[indices_aleatorios].astype(float)

        for iteracao in range(self.max_iter):
            labels = []

            # Aqui, vamos calcular a distância e encontrar o grupo mais perto
            for ponto in X:
                distancias = [np.linalg.norm(ponto - centroide) for centroide in self.centroids]
                grupo_mais_perto = np.argmin(distancias)
                labels.append(grupo_mais_perto)

            labels = np.array(labels)
            novos_centroides = []

            # Ainda dentro do loop, vamos calcular os novos centroides
            for grupo in range(self.n_clusters):
                pontos_do_grupo = X[labels == grupo]
                if len(pontos_do_grupo) > 0:
                    media = np.mean(pontos_do_grupo, axis=0)
                    novos_centroides.append(media)
                else:
                    novos_centroides.append(self.centroids[grupo])

            novos_centroides = np.array(novos_centroides)
            
            deslocamento = np.linalg.norm(novos_centroides - self.centroids)
            
            # Parte da decisão da convergência
            if deslocamento < self.tol:
                break

            self.centroids = novos_centroides

        return labels

