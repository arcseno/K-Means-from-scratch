'''
[Ex2] Algoritmo K-Means - Aprendizado de Máquina Não Supervisionado - Profº
Gustavo Taiji Naozuka

---------------------------------------------------------------------------

** PLANNING **

1º STEP:

-> O Método fit_predict(x) deve implementar o agrupamento de dados com o
K-Means. Como fazer isso?

    * Deve realizar a inicialização aleatória, escolhendo K pontos (baseado no n_clusters) do conjunto de dados X para serem os centroides iniciais. Aqui dá pra utilizar o random choice do numpy.

    * Depois, para cada ponto do conjunto de dados X, nós calculamos a distância euclidiana em relação a cada um dos K centroides.
    Assim, atribui o ponto ao centroide mais proximo. 

    * Logo após, para cada grupo criado na etapa anterior, calcular a média aritmética das coordenadas de todos os pontos que pertencem a ele. E, finalmente, mover o centroide desse grupo para a nova posição média desse cálculo.

    * O critério de parada, a dita convergência, acontecerá quando:
        -> Os centroides pararam de se mover (a diferença entre a posição antiga e a nova é < que a tolerância dada)
        -> O número máximo de repetições max_iter for atingido.

2º STEP:

-> Testar a classe implementada no conjunto de dados do exemplo: Segmentação
de Clientes de Academia.

3º STEP:

-> Fazer um gráfico de dispersão, em que cada ponto é colorido de acordo com o
cluster encontrado, e devem ter os centroides finais (após convergir) com um 
símbolo diferente.

ENTREGA:

-> Dois arquivos, um KMeans.py e uma main.py
-> Compactar ambos e entregar em um arquivo KMeans_ViniciusOya.zip

---------------------------------------------------------------------------

'''

import numpy as np

class KMeans:
    def __init__(self, n_clusters=3, max_iter=300, tol=0.0001):
        self.n_clusters = n_clusters
        self.max_iter = max_iter
        self.tol = tol
        self.centroids = None

    def fit_predict(self, X):
        # Etapa de inicialização randômica dos centróides:
        indices = np.random.choice(len(X), self.n_clusters, replace=False)
        self.centroids = X[indices]

        # O limite máximo de iteração é o hiperparametro de max_iter, e vai acabar ou ao final do loop, ou qnd convergir de acordo com a tolerância dada
        for i in range(self.max_iter):

        
    
        #return labels

