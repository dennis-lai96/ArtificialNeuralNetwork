class Node:
    def __init__(self, connections):
        self.collector = 0.0
        self.connections = connections


def print_array_of_arrays(arrays):
    for array in arrays:
        print(array)


if __name__ == "__main__":
    network_structure = []

    #Open up the file and turn it in to an int list.
    f = open("NumNodes", "r")
    network_structure = [int(num) for num in f.read().split(",")]
    print(network_structure)
    f.close()
    print("Network structure is of type", type(network_structure))
    #Open up the file and turn it in to a float list.


    f = open("InitialValues", "r")
    initial_values = [float(num) for num in f.read().split(",")]
    # Now we need to make an empty Node array of arrays using this.

    network = [[0] * size for size in network_structure]
    numLayers = len(network)

    print_array_of_arrays(network)




    #this will iterate through the number of layers the neural network contains
    for i in range(numLayers):
        # Starting Layer
        if i == 0:
            print("Network 0: ")
            sum = 0
            #Sets Layer 0's array values to initial values and points it to the next array
            for j in range(len(initial_values)):
                x = initial_values[j]
                network[0][j] = Node(network[i + 1])
                network[0][j].collector = x

                print("Network", i, j, "has this connection:", network[0][j].connections)
                print("Network", i, j, " has this collector val: ", network[0][j].collector)
        #hidden layer
        elif i < numLayers-1:  # i is going to be 1 in this case, which is smaller than 2
            print("Network ", i, ": ")
            #iterates through the current network. Sets Node connection to next array
            for j in range(len(network[i])):
                    network[i][j]=Node(network[i+1])
                    #Collector in this will accumulate itself with the PREVIOUS layer's collector values.
                    for k in range(len(network[i-1])):
                        network[i][j].collector = network[i][j].collector+ network[i-1][k].collector
                    print("Network", i, j, "has this connection:", network[i][j].connections)
                    print("Network", i, j, " has this collector val: ", network[i][j].collector)


        #Last Layer
        else:
            print("Last layer: ")
            for j in range(len(network[i])):
                #Creates Nodes in all of array slots pointing to None since it's the last layer.
                network[i][j] = Node(None)
                print("Network", i, j, "has this connection:", network[i][j].connections)
                #Same collector method as before. could probably make this a method
                for k in range(len(network[i-1])):
                    network[i][j].collector = network[i][j].collector+ network[i-1][k].collector
                    print("Network", i, j, " has this collector val: ", network[i][j].collector)



    #Printing All results
    for i in range(numLayers):
        print("This is network[", i,"] ", network[i])

    for i in range(numLayers):
        for j in range(len(network[i])):
            print("Network[", i, "][", j, "] connections", network[i][j].connections)

    for i in range(numLayers):
        for j in range(len(network[i])):
            print("Network[", i, "][",j,"] collector value", network[i][j].collector)




