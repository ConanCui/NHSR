import numpy  as np
import activeFunction as af
def WNMF(R,k = 20):
    # Index matrix for training data
    I = R.copy()
    I[I > 0] = 1
    I[I == 0] = 0

    # paramets
    m,n = R.shape
    lamda = 8
    n_epochs = 150 # Number of epochs
    # use stochastic initialization
    P = np.random.rand(m, k) + 10**-4  # Latent user feature matrix
    Q = np.random.rand(k, n) + 10**-4  # Latent movie feature matrix

    # factorazation
    for epoch in xrange(n_epochs):
        # updata Q
        PTR = np.dot(P.T,R*I)
        PTIPQ = np.dot(P.T,I*np.dot(P,Q))+ lamda * Q + 10**-9
        Q = Q* (PTR/PTIPQ)

        # updata P
        RQT = np.dot(I*R,Q.T)
        WPQQT = np.dot(I*np.dot(P,Q),Q.T) + lamda * P + 10**-9
        P = P * (RQT/WPQQT)


    return P,Q

class wnmf(af.activationFunction):
    def __init__(self,n_epochs_wnmf = 150,lamda_wnmf = 8 ,gama =1, beta =1 , type = 'linear' ):
        af.activationFunction.__init__(self, gama, beta, type)
        self.n_epochs_wnmf = n_epochs_wnmf
        self.lamda_wnmf = lamda_wnmf
    def WNMF(self,R , k):
        # Index matrix for training data
        I = R.copy()
        I[I > 0] = 1
        I[I == 0] = 0

        # paramets
        m, n = R.shape

        # use stochastic initialization
        P = np.random.rand(m, k) + 10 ** -4  # Latent user feature matrix
        Q = np.random.rand(k, n) + 10 ** -4  # Latent movie feature matrix

        # factorazation
        for epoch in xrange(self.n_epochs_wnmf):
            # updata Q
            PTR = np.dot(P.T, R * I)
            PTIPQ = np.dot(P.T, I * np.dot(P, Q)) + self.lamda_wnmf * Q + 10 ** -9
            Q = Q * (PTR / PTIPQ)

            # updata P
            RQT = np.dot(I * R, Q.T)
            WPQQT = np.dot(I * np.dot(P, Q), Q.T) + self.lamda_wnmf * P + 10 ** -9
            P = P * (RQT / WPQQT)

        return P, Q




