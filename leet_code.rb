# Returns an array of valid parenthesis patterns with n pairs of parenthesis
def generate_parenthesis(n)
    return ["()"] if n == 1
    res = []
    parens = generate_parenthesis(n - 1)
    parens.each do |p|
        res << "()" + p
        res << p + "()"
        res << "(" + p + ")"
    end
    res.uniq.sort
end

# Find the lowest common ancenstor between two nodes in a tree where nodes reference parent
def lowest_common_ancestor(node1, node2)
  # Find the differences in depth between two nodes
  depth_diff = count_depth(node1) - count_depth(node2)
  x = node1
  y = node2
  # Give the deeper node pointer a headstart
  if depth_diff > 1
    depth_diff.times { x = x.parent }
  else
    (depth_diff * -1).times do { y = y.parent }
  end
  # Climb up the tree until reach common ancestor
  until x == y
    x = x.parent
    y = y.parent
  end
  x
end

def count_depth(node)
  depth = 0
  current_node = node
  until node.parent.nil?
    current_node = node.parent
    depth += 1
  end
  depth
end

# Take an array of intervals and merge any that overlap
class Interval
  attr_accessor :start, :end
  def initialize(s = 0, e = 0)
    @start = s
    @end = e
  end
end

def merge(intervals)
  intervals.sort! { |x, y| x.start <=> y.start }
  res = []
  queue = []
  intervals.each do |int|
    if queue.empty?
      res << Interval.new(int.start)
      queue << int.end
    elsif int.start <= res.last.end
      if int.end > res.last.end
        res.last.end = int.end
      end
    elsif int.start <= queue.last
      queue << int.start
      if int.end >= queue.first
        res.last.end = int.end
        queue = []
      else
        queue << int.end
      end
    elsif int.start > queue.first
      res.last.end = queue.first
      res << Interval.new(int.start)
      queue = [int.end]
    end
  end
  res.last.end = queue.first unless queue.empty?
  res
end
