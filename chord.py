class ChordNode:
    def __init__(self, node_id, successors, predecessor, data):
        self.node_id = node_id
        self.successors = successors
        self.predecessor = predecessor
        self.data = data

    def find_successor(self, key):
        if key in self.successors:
            return self.successors[key]
        else:
            filtered = filter(lambda x: x > key, self.successors.keys())
            print(list(filtered))  # Print the values of the filtered list
            if not filtered:
                if not self.successors:
                    print("self.successors is empty")
                return self.successors[min(self.successors.keys())]
            else:
                return self.successors[min(filtered)]

    def join(self, network):
        if not network.nodes:
            network.add_node(self)
            return

        successor = network.nodes[0]
        for node in network.nodes.values():
            if self.node_id < node.node_id < successor.node_id:
                successor = node

        self.successors[successor.node_id] = successor
        self.predecessor = successor.predecessor
        successor.predecessor = self

        network.add_node(self)

    def leave(self, network):
        for successor in self.successors.values():
            successor.predecessor = self.predecessor
        self.predecessor.successors.update(self.successors)
        network.remove_node(self)

    def lookup(self, education_data, education, min_aw, max_aw, min_sur, max_sur):
        scientists_data = self.data
        # print(scientists_data)
        # find the surnames of scientists whose education list contains the string of variable education
        surnames = [scientist.surname for scientist in scientists_data if
                    education in scientist.education and scientist.awards > min_aw and scientist.awards < max_aw and max_sur> scientist.surname > min_sur]

        # print(surnames)
        return surnames


class ChordNetwork:
    def __init__(self):
        self.nodes = {}

    def add_node(self, node):
        self.nodes[node.node_id] = node

    def remove_node(self, node):
        del self.nodes[node.node_id]

    def chord_lookup(self, education_data, education, min_aw, max_aw, min_sur, max_sur):
        return self.nodes[0].lookup(education_data, education, min_aw, max_aw, min_sur, max_sur)
