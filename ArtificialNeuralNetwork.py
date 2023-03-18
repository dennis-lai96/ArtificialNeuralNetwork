class Node:
    def __init__(self,connections):
        self.collector = 0.0
        self.connections = None
def print_array_of_arrays(arrays):
    for array in arrays:
        print(array)


if __name__ == "__main__":
    network_structure = []
    f = open("NumNodes", "r")
    #figure out txt to array later...
    print(f.read().split(','))


    network_structure = [4,2,1]
    initial_values =  [4.1, 5.5, 3.3, 10.01 ]
    #Now we need to make an empty Node array of arrays using this.

    network = [ [0] * size for size in network_structure]

    node = ([Node])

    network[0][0] = node



    print_array_of_arrays(network)
    print(type(network))

    #The loop should look seomthing like
    #for: int i = 0, i < network_list_max(the size of the array of arrays), i++
        #if int i = 0, array[0] acccumulators receiv other list's values(10.1,4.2,whatever)
        #if int i > 0, array[i] receives array[i-1]'s first address.
        #afterwards, array[i] nodes all receive in accumulator, all the values from previous arrays accumulators.

    # for i in range(len(network)):
    #     if i==0:
    #         for j in range(len(initial_values)):
    #             print()

                #network[0][j] = initial_values[j]





    print_array_of_arrays(network)