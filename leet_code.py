class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class GraphCloneSolution:
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


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        median1 = self.findMedian(nums1)
        median2 = self.findMedian(nums2)
        return (median1 + median2) / 2.0

    def findMedian(nums):
        if len(nums) % 2 == 0:
            i = len(nums) / 2 - 1
            j = len(nums) / 2
            return (nums[i] + nums[j]) / 2.0
        else:
            i = int(len(nums) / 2)
            return nums[i]
