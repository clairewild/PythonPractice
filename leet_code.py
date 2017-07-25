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

# Create an itterator that itterates over a BST and returns all elements in order
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
                elif current_node.left.right and self.seen_vals[-1] == current_node.left.val:
                    current_node = current_node.left

            elif current_node.val not in self.seen_vals:
                break
            elif current_node.right:
                current_node = current_node.right

        self.seen_vals.append(current_node.val)
        return current_node.val

# Better BST itterator that returns next smallest value
class BSTIterator(object):
    def __init__(self, root):
        # Create stack of all nodes down the left most side
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left

    def hasNext(self):
        return len(self.stack) > 0

    def next(self):
        node = self.stack.pop()
        # Add nodes down the left most side from the right child of node being returned
        x = node.right
        while x:
            self.stack.append(x)
            x = x.left
        return node.val

# Take a two dimentional array of 0's and 1's and return number of "islands" (adjacent sections of 1's)
class IslandsSolution(object):
    def numIslands(self, grid):
        self.grid = grid
        self.seen = {}
        islands = 0
        for row in range(0, len(self.grid)):
            for col in range(0, len(self.grid[row])):
                if self.grid[row][col] == 1 and (row, col) not in self.seen:
                    islands += 1
                    self.exploreIsland(row, col)
        return islands

    def exploreIsland(self, row, col):
        if self.grid[row][col] == 0 or (row, col) in self.seen: return
        self.seen[(row, col)] = True
        for adj in self.adjacents(row, col):
            self.exploreIsland(adj[0], adj[1])

    def inBounds(self, row, col):
        height = len(self.grid)
        width = len(self.grid[0])
        return 0 <= row < height and 0 <= col < width

    def adjacents(self, row, col):
        diffs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        adjacents = map(lambda diff: [row + diff[0], col + diff[1]], diffs)
        return filter(lambda pos: self.inBounds(pos[0], pos[1]), adjacents)

# grid1 = [[1,1,1,1,0], [1,1,0,1,0], [1,1,0,0,0], [0,0,0,0,0]]
# grid2 = [[1,1,0,0,0], [1,1,0,0,0], [0,0,1,0,0], [0,0,0,1,1]]
#
# i = IslandsSolution()
# print(i.numIslands(grid1))
# print(i.numIslands(grid2))
