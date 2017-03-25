import numpy as np
import pandas as pd
from sklearn import cross_validation as cv
import matplotlib.pyplot as plt

header = ['user_id', 'item_id', 'rating', 'timestamp']
df = pd.read_csv('./ml-100k/ml-100k/u.data', sep='\t', names=header)
n_users = df.user_id.unique().shape[0]
n_items = df.item_id.unique().shape[0]
print 'Number of users = ' + str(n_users) + ' | Number of movies = ' + str(n_items)

train_data, test_data = cv.train_test_split(df, test_size=0.4)
train_data = pd.DataFrame(train_data)
test_data = pd.DataFrame(test_data)

# Create training and test matrix
R = np.zeros((n_users, n_items))
for line in train_data.itertuples():
    R[line[1] - 1, line[2] - 1] = line[3]

T = np.zeros((n_users, n_items))
for line in test_data.itertuples():
    T[line[1] - 1, line[2] - 1] = line[3]

# R = np.array([[1,0,3,4],
#      [5,0,7,8],
#      [9,10,0,12]])
# T = np.array([[0,2,0,0],
#      [0,2,0,0],
#      [0,0,2,0]])

class NonlinearFunction:
    def __init__(self):
        pass

    # def Fun(self, X):
    #     return (X) * (X)
    #
    # def Derivative(self, X):
    #     return 2 * (X)

    # def Fun(self,X):
    #     return (X)
    # def Derivative(self,X):
    #     return 1
    def Fun(self,X):
        return 1.5 * (np.exp(X) - np.exp(-X))/(np.exp(X) + np.exp(-X))
    def Derivative(self,X):
        temp = 1.5 * (np.exp(X) - np.exp(-X))/(np.exp(X) + np.exp(-X))
        return 1.5*1.5 - temp**2

# Index matrix for training data
I = R.copy()
I[I > 0] = 1
I[I == 0] = 0

# Index matrix for test data
I2 = T.copy()
I2[I2 > 0] = 1
I2[I2 == 0] = 0

def prediction(P, Q):
    return np.dot(P, Q)

k  = 20
m,n = R.shape
P = 3 * np.random.rand(m, k) + 10**-9
Q = 3 * np.random.rand(k, n) + 10**-9
n_epochs = 100  # Number of epochs

# Calculate the RMSE
def rmse(I, R, Q, P):
    return np.sqrt(np.sum((I * (R - FunX2.Fun(prediction(P, Q)))) ** 2) / len(R[R > 0]))

train_errors = []
test_errors = []
FunX2 = NonlinearFunction()

for epoch in xrange(n_epochs):

    # updata Q
    PQ = np.dot(P, Q)
    RQT = np.dot(R * FunX2.Derivative(PQ), Q.T)
    WPQQT = np.dot(FunX2.Fun(PQ) * FunX2.Derivative(PQ), Q.T) + 10 ** -9
    P = P * (RQT / WPQQT) ** 0.8

    # updata P
    PQ = np.dot(P, Q)
    PTR = np.dot(P.T, R * FunX2.Derivative(PQ))
    PTIPQ = np.dot(P.T, FunX2.Fun(PQ) * FunX2.Derivative(PQ)) + 10 ** -9
    Q = Q * (PTR / PTIPQ) ** 0.8

    train_rmse = rmse(I,R,Q,P)
    test_rmse = rmse(I2,T,Q,P)
    train_errors.append(train_rmse)
    test_errors.append(test_rmse)
    print epoch, "test_rmse", test_rmse,"train_rmse", train_rmse

plt.plot(range(n_epochs), train_errors, marker='o', label='Training Data');
plt.plot(range(n_epochs), test_errors, marker='v', label='Test Data');
plt.text(n_epochs - 1, train_errors[-1], str(train_errors[-1]),horizontalalignment='center',verticalalignment='top')
plt.text(n_epochs - 1, test_errors[-1], str(test_errors[-1]),horizontalalignment='center',verticalalignment='top')

plt.title('NMF Learning Curve')
plt.xlabel('Number of Epochs');
plt.ylabel('RMSE');
plt.legend()
plt.grid()
plt.show()

print R
print np.dot(P,Q)

