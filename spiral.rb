# Draw a spiral
class Spiral
  def initialize(size)
    @grid = []
    @size = size
    @dir_map = {
      right: :down,
      down: :left,
      left: :up,
      up: :right
    }
    self.create_grid
  end

  def create_grid
    @size.times do
      @grid << ["-"] * @size
    end
  end

  def create_spiral
    self.fill_row(0, 0, :right)
    self.print
  end

  def fill_row(start_i, start_j, dir)
    i = start_i
    j = start_j
    filled = 0
    case dir
    when :down
      until stop_drawing(i, j, dir)
        @grid[i][j] = "x"
        i += 1
        filled += 1
      end
      i -= 1
    when :left
      until stop_drawing(i, j, dir)
        @grid[i][j] = "x"
        j -= 1
        filled += 1
      end
      j += 1
    when :up
      until stop_drawing(i, j, dir)
        @grid[i][j] = "x"
        i -= 1
        filled += 1
      end
      i += 1
    when :right
      until stop_drawing(i, j, dir)
        @grid[i][j] = "x"
        j += 1
        filled += 1
      end
      j -= 1
    end
    fill_row(i, j, @dir_map[dir]) if filled > 1
  end

  def stop_drawing(i, j, dir)
    return true unless @grid[i] && @grid[i][j]
    case dir
    when :down
      return true if @grid[i + 1] && @grid[i + 1][j] == "x"
    when :left
      return true if @grid[i][j - 1] == "x"
    when :up
      return true if @grid[i - 1] && @grid[i - 1][j] == "x"
    when :right
      return true if @grid[i][j + 1] == "x"
    end
    false
  end

  def print
    @grid.each do |row|
      puts row.join
    end
  end
end

s = Spiral.new(10)
s.create_spiral
