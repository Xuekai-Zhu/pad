def solution():
    total_flour = 200 + 100 + 100  # (in g)
    flour_per_loaf = 200  # (in g)
    num_loaves = total_flour // flour_per_loaf
    result = num_loaves
    return result

print(solution())