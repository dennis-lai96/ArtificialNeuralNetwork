class Node:
    def __init__(self, connections):
        self.collector = 0.0
        self.connections = connections


def print_array_of_arrays(arrays):
    for array in arrays:
        print(array)


if __name__ == "__main__":
    network_structure = []
    # f = open("NumNodes", "r")
    # #figure out txt to array later...
    # print(f.read().split(','))

    network_structure = [4, 2, 1]
    initial_values = [4.1, 5.5, 3.3, 10.01]
    # Now we need to make an empty Node array of arrays using this.

    network = [[0] * size for size in network_structure]
    numLayers = len(network)
    print("nubmer of layers: ", numLayers)
    print_array_of_arrays(network)
    print(type(network))
    print("array[1] is ", network[1])
    # The loop should look seomthing like
    # for: int i = 0, i < network_list_max(the size of the array of arrays), i++
    # if int i = 0, array[0] acccumulators receiv other list's values(10.1,4.2,whatever)
    # if int i > 0, array[i] receives array[i-1]'s first address.
    # afterwards, array[i] nodes all receive in accumulator, all the values from previous arrays accumulators.

    for i in range(numLayers):
        if i == 0:
            sum = 0
            for j in range(len(initial_values)):
                x = initial_values[j]
                network[0][j] = Node(network[i + 1])
                network[0][j].collector = x
                print("Network", i, j, "has this connection:", network[0][j].connections)
                print("Network", i, j, " has this collector val: ", network[0][j].collector)

        elif i+1 < numLayers:  # i is going to be 1 in this case, which is smalelr than 2
            print("Network 2: ")
            for j in range(len(network[i])):
                    network[i][j]=Node(network[i+1])
                    print("Network", i, j, "has this connection:", network[i][j].connections)
                    print("Network", i, j, " has this collector val: ", network[i][j].collector)

        else:
            for j in range(len(network[i])):
                print("wtf")
                network[i][j] = Node(None)
                print("Network", i, j, "has this connection:", network[i][j].connections)
                print("Network", i, j, " has this collector val: ", network[i][j].collector)




    print("this is network 0 ", network[0])
    print("this is network 1 ", network[1])
    print("this is network 2 ", network[2])

    print("This is network 0-0 connections: ", network[0][0].connections)
    print("This is network 0-1 connections: ", network[0][1].connections)
    print("This is network 0-1 connections: ", network[0][2].connections)
    print("This is network 0-1 connections: ", network[0][3].connections)

    print("This is network 1-0 connections: ", network[1][0].connections)
    print("This is network 1-1 connections: ", network[1][1].connections)


    print("value [0][0]", network[0][0].collector)
    print("value [0][1]", network[0][1].collector)
    print("value [0][2]", network[0][2].collector)
    print("value [0][3]", network[0][3].collector)
