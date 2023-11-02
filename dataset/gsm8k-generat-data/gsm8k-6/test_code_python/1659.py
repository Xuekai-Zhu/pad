def solution():
    pines = 600  # number of pines in the national park
    redwoods = 1.2 * pines  # number of redwoods is 20% more than the number of pines
    total_trees = pines + redwoods  # total number of trees
    result = (pines, redwoods, total_trees)
    return result

print(solution())