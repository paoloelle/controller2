import numpy as np

class ANN_controller:
    def __init__(self, input_size, hidden_size, output_size):
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size

    def upload_parameters(self, genome):
        # todo here I have a list of values (a genome and I have to split it to have W1, b1, W2, b2)
        W1 = 
        b1 = 
        W2 = 
        b2 = 

        parameters = [W1, b1, W2, b2]

        return parameters

    def forward(self, X, parameters):
        W1, b1, W2, b2 = parameters

        # activation function hidden layer
        Z1 = np.dot(X, W1) + b1  # X row vector, Z column vector
        A1 = np.tanh(Z1)

        # activation function output layer
        Z2 = np.dot(A1, W2) + b2
        A2 = Z2 # regression problem, linear function

        return A2
