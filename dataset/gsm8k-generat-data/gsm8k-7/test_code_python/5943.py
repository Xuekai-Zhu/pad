def solution():
    total_lollipops = 42
    cherry_lollipops = total_lollipops / 2
    other_lollipops = total_lollipops - cherry_lollipops
    num_flavors = 3
    grape_lollipops = other_lollipops / num_flavors
    result = grape_lollipops
    return result

print(solution())