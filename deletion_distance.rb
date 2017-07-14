def ascii_deletion_distance(str1, str2)
  chars_to_delete = reduce_strings(str1, str2)
  return chars_to_delete.sum
end

def reduce_strings(str1, str2)
  shared_chars = create_hashmap(str1, str2)
  return str1 + str2 if shared_chars.keys.none? { |key| shared_chars[key] == true }

  shared_chars.each do |char, val|
    if val == true
      str1.sub!(char, "")
      str2.sub!(char, "")
    end
  end
  reduce_strings(str1, str2)
end

# Runs in linear time, n + m, with worst case linear space complexity
def create_hashmap(str1, str2)
  shared_chars = {}
  str1.split("").each do |char|
    shared_chars[char] = "str1"
  end
  str2.split("").each do |char|
    if shared_chars[char]
      shared_chars[char] = true
    else
      shared_chars[char] = "str2"
    end
  end
  shared_chars
end
