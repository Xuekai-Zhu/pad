def solution():
    total_children = 50
    boys_fraction = 3/5
    girls_fraction = 1 - boys_fraction

    girls_count = int(girls_fraction * total_children)
    result = girls_count
    return result

print(solution())