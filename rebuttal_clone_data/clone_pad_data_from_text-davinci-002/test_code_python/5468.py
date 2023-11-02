def solution():
    trees = 8
    oranges_per_tree = 200
    fraction_picked = 2/5
    oranges_left = (oranges_per_tree * trees) * (1 - fraction_picked)
    result = oranges_left
    return result

print(solution())