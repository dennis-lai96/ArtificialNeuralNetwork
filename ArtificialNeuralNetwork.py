class Node:
    def __init__(self,connections):
        self.collector = 0.0
        self.connections = connections

if __name__ == "__main__":
    network_structure = []
    f = open("NumNodes", "r")

    print(f.read().split(','))
    
