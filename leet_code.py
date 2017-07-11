class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution:
    def cloneGraph(self, node):
        new_node = UndirectedGraphNode(node.label)
        nodes_dict = {}
        queue = []

        nodes_dict[new_node.label] = new_node
        queue.append(node)

        while queue.length > 0:
            current_node = queue.pop(0)

            for neighbor in current_node.neighbors:
                if neighbor.label not in nodes_dict:
                    nodes_dict[neighbor.label] = UndirectedGraphNode(neighbor.label)
                    queue.append(neighbor)

                nodes_dict[current_node.label].neighbors.append(nodes_dict[neighbor.label])

        return new_node
