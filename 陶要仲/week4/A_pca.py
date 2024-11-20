import numpy as np

class PCA(object):

    def __init__(self, X, K):
        self.X = X
        self.K = K
        self.central_x = []
        self.C = []
        self.U = []
        self.Z = []

        self.central_x = self._centralized()
        self.C = self._cov()
        self.U = self._U()
        self.Z = self._Z()

    def _centralized(self):
        print('样本矩阵X:\n', self.X)
        centralX = []
        mean = np.array([np.mean(attr) for attr in self.X.T])  # 样本集的特征均值
        print('样本集的特征均值:\n', mean)
        centralX = self.X - mean  ##样本集的中心化
        print('样本矩阵X的中心化centrX:\n', centralX)
        return centralX

    # 中心化矩阵求协方差矩阵（C= 1/m * Z.T * Z）
    def _cov(self):
        ns = np.shape(self.central_x)[0]
        # 协方差矩阵C
        C = np.dot(self.central_x.T, self.central_x)/(ns - 1)
        print('样本矩阵X的协方差矩阵C:\n', C)
        return C

    def _U(self):
        '''求X的降维转换矩阵U, shape=(n,k), n是X的特征维度总数，k是降维矩阵的特征维度'''
        #先求X的协方差矩阵C的特征值和特征向量
        a,b = np.linalg.eig(self.C) #特征值赋值给a，对应特征向量赋值给b。函数doc：https://docs.scipy.org/doc/numpy-1.10.0/reference/generated/numpy.linalg.eig.html
        print('样本集的协方差矩阵C的特征值:\n', a)
        print('样本集的协方差矩阵C的特征向量:\n', b)
        print(b[:,1])
        #给出特征值降序的topK的索引序列
        ind = np.argsort(-1*a)
        #构建K阶降维的降维转换矩阵U
        UT = [b[:,ind[i]] for i in range(self.K)]
        U = np.transpose(UT)
        print('%d阶降维转换矩阵U:\n'%self.K, U)
        return U

    def _Z(self):
        '''按照Z=XU求降维矩阵Z, shape=(m,k), n是样本总数，k是降维矩阵中特征维度总数'''
        Z = np.dot(self.X, self.U)
        print('X shape:', np.shape(self.X))
        print('U shape:', np.shape(self.U))
        print('Z shape:', np.shape(Z))
        print('样本矩阵X的降维矩阵Z:\n', Z)
        return Z

if __name__=='__main__':
    '10样本3特征的样本集, 行为样例，列为特征维度'
    X = np.array([[10, 15, 29],
                  [15, 46, 13],
                  [23, 21, 30],
                  [11, 9,  35],
                  [42, 45, 11],
                  [9,  48, 5],
                  [11, 21, 14],
                  [8,  5,  15],
                  [11, 12, 21],
                  [21, 20, 25]])
    K = np.shape(X)[1] - 1
    print('样本集(10行3列，10个样例，每个样例3个特征):\n', X)
    pca = PCA(X,K)
