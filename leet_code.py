# Clone an undirected graph
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

# Find the median of two sorted arrays in O(logn) time complexity
class MedianSolution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        median1 = self.findMedian(nums1)
        median2 = self.findMedian(nums2)
        res = (median1 + median2) / 2.0
        return round(res, 1)

    def findMedian(self, nums):
        if len(nums) % 2 == 0:
            i = len(nums) / 2 - 1
            j = len(nums) / 2
            return (nums[i] + nums[j]) / 2.0
        else:
            i = int(len(nums) / 2)
            return nums[i]

class BetterMedianSolution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        arr = self.merge(nums1, nums2)
        if len(arr) == 0:
            return None
        if len(arr) % 2 == 0:
            i = len(arr) / 2 - 1
            j = len(arr) / 2
            return (arr[i] + arr[j]) / 2.0
        else:
            i = int(len(arr) / 2)
            return arr[i]

    def merge(self, nums1, nums2):
        arr = []
        while len(nums1) > 0 and len(nums2) > 0:
            if nums1[0] <= nums2[0]:
                arr.append(nums1.pop(0))
            else:
                arr.append(nums2.pop(0))
        return arr + nums1 + nums2

# Create an itterator that itterates over a BST
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BSTIterator(object):
    def __init__(self, root):
        self.root = root
        self.max = self.findMax
        self.seen_vals = []

    def findMax(self):
        current_node = self.root
        while current_node.right:
            current_node = current_node.right
        return current_node

    def hasNext(self):
        return self.max not in self.seen_vals

    def next(self):
        current_node = self.root
        while current_node.left or current_node.right:
            if current_node.left:
                if current_node.left.val not in self.seen_vals:
                    current_node = current_node.left
                else if current_node.left.right and seen_vals[-1] == current_node.left.val:
                    current_node = current_node.left

            else if current_node.val not in self.seen_vals:
                break
            else if current_node.right:
                current_node = current_node.right

        self.seen_vals.append(current_node.val)
        return current_node.val
