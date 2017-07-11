class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution:
    # @param node, an undirected graph node
    # @return an undirected graph node
    def cloneGraph(self, node):
        new_node = UndirectedGraphNode(node.label)
        nodes_dict = {}
        stack = []

        nodes_dict[new_node.label] = new_node
        stack.append(node)

        while stack.length > 0:
            current_node = stack.pop()

            for neighbor in current_node.neighbors:
                if !nodes_dict[neighbor.label]:
                    nodes_dict[neighbor.label] = UndirectedGraphNode(neighbor.label)
                    stack.append(neighbor)

                nodes_dict[current_node.label].neighbors.append(nodes_dict[neighbor.label])

        return new_node
