from Web_Crawler import generate_data


class PastryNode(object):
    def __init__(self, node_id, scientists):
        self.node_id = node_id
        self.routing_table = {}
        self.leaf_set = []
        self.neighborhood_set = []
        self.scientists = scientists

    def join(self, pastry_network):
        pass

    def leave(self, pastry_network):
        pass

    def lookup(self, key, threshold, max_aw, min_sur, max_sur):
        results = []
        for scientist in self.scientists:
            if key in scientist.education and threshold < scientist.awards:
                if scientist.awards < max_aw:
                    if min_sur < scientist.surname < max_sur:
                        results.append(scientist)
                        return results


class PastryNetwork(object):
    def __init__(self):
        self.nodes = {}

    def add_node(self, node):
        self.nodes[node.node_id] = node

    def remove_node(self, node):
        del self.nodes[node.node_id]

    def lookup(self, key, threshold, max_aw, min_sur, max_sur):
        results = []
        for node in self.nodes.values():
            results += node.lookup(key, threshold, max_aw, min_sur, max_sur)
        return results
