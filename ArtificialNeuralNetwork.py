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


if __name__ == "__main__":
    print("MAKING THE NEURAL NETWORK")
    nn = NeuralNetwork("NumNodes", "InitialValues")
    nn.print_array_of_arrays()
    nn.print_results()