'''
[Ex2] Algoritmo K-Means - Aprendizado de Máquina Não Supervisionado - Profº
Gustavo Taiji Naozuka

---------------------------------------------------------------------------

** PLANNING **

1º STEP:

-> O Método fit_predict(x) deve implementar o agrupamento de dados com o
K-Means. Como fazer isso?

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
    def __init__(self, n_clusters, max_iter, tol, centroids):
        self.n_clusters = n_clusters
        self.max_iter = max_iter
        self.tol = tol
        self.centroids = centroids

    # def fit_predict(X):
