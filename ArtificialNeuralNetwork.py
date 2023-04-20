import random

class Node:
    def __init__(self, connections):
        self.collector = 0.0
        self.connections = connections
        self.weight = 1.0


class NeuralNetwork:
    def __init__(self, num_nodes_file, initial_values_file):
        self.network_structure = self.read_integer_list(num_nodes_file)
        self.initial_values = self.read_float_list(initial_values_file)
        self.network = self.build_network()

    def read_integer_list(self, filename):
        with open(filename, "r") as f:
            return [int(num) for num in f.read().split(",")]

    def read_float_list(self, filename):
        with open(filename, "r") as f:
            return [float(num) for num in f.read().split(",")]

    def build_network(self):
        network = [[0] * size for size in self.network_structure]
        num_layers = len(network)

        for i in range(num_layers):
            if i == 0:
                for j in range(len(self.initial_values)):
                    x = self.initial_values[j]
                    network[0][j] = Node(network[i + 1])
                    network[0][j].collector = x
                    network[0][j].weight = random.uniform(0, 1)
            elif i < num_layers-1:
                for j in range(len(network[i])):
                    network[i][j] = Node(network[i+1])
                    network[i][j].weight = random.uniform(0, 1)
                    for k in range(len(network[i-1])):
                        network[i][j].collector += (network[i-1][k].collector * network[i-1][k].weight)
            else:
                for j in range(len(network[i])):
                    network[i][j] = Node(None)
                    network[i][j].weight = random.uniform(0, 1)
                    for k in range(len(network[i-1])):
                        network[i][j].collector += (network[i-1][k].collector * network[i-1][k].weight)
        return network

    def print_array_of_arrays(self):
        for array in self.network:
            print(array)

    def print_results(self):
        num_layers = len(self.network)
        for i in range(num_layers):
            print(f"This is network[{i}]", self.network[i])
        for i in range(num_layers):
            for j in range(len(self.network[i])):
                print(f"Network[{i}][{j}] connections:", self.network[i][j].connections)
        for i in range(num_layers):
            for j in range(len(self.network[i])):
                print(f"Network[{i}][{j}] weight value:", self.network[i][j].weight)
        for i in range(num_layers):
            for j in range(len(self.network[i])):
                print(f"Network[{i}][{j}] collector value:", self.network[i][j].collector)


    def forward_propagate(self, inputs):
        #Setting input values to the first layer's collector values
        for i in range(len(inputs)):
            self.network[0][i].collector = inputs[i]
        #Accumulates similar to the build-network func
        for i in range(1, len(self.network)):
            for j in range(len(self.network[i])):
                collector = 0.0
                for k in range(len(self.network[i-1])):
                    collector += (self.network[i-1][k].collector * self.network[i-1][k].weight)
                self.network[i][j].collector = collector

    #code given by prof may need to modify
    def train_network(self, train, l_rate, n_epoch, target_error):
        number_of_inputs = len(self.network[0])
        for epoch in range(n_epoch):
            sum_error = 0
            for row in train:
                self.forward_propagate(row)
                expected = []
                for i in range(len(self.network[-1])):
                    expected.append(row[number_of_inputs + i])
                    sum_error += (row[number_of_inputs + i] - self.network[-1][i].collector)**2
                if sum_error <= target_error:
                    print("Target Error Reached error=%.3f" % (sum_error))
                    return
                self.backwardPropogate_error(expected)
                self.update_weights()(l_rate)
            print('>epoch=%d, lrate=%.3f, error=%.3f' % (epoch, l_rate, sum_error))


    def backwardPropogate_error(self,expected   ):
        for i in reversed(len(self.network)):
            layer = self.network[i]
            errors = []
            #basically if we're not in the last layer
            if i !=len(self.network)-1:
                #iterating through every other layers(not the last) errors in each node
                for j in range(len(layer)):
                    error = 0.0
                    for neuron in self.network[i+1]:
                        error+=(neuron.weight*neuron.delta)
                    errors.append(error)
            else: #dealing with the last layer's neruons
                for j in range(len(layer)):
                    neuron=layer[j]
                    #expected last 0 or 1 minus whatever we have on the last neuron
                    errors.append(expected[j]-neuron.collector)




    def update_weights(self,l_rate):
        return "hahahahahahahahahah"

if __name__ == "__main__":
    print("MAKING THE NEURAL NETWORK")
    nn = NeuralNetwork("NumNodes", "InitialValues")
    nn.print_array_of_arrays()
    nn.print_results()