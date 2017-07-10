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
