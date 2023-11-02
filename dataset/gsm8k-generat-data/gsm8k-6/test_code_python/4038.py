def solution():
    # Let x be the number of geese in the initial V formation
    # Half of the geese landed, so there are now x/2 geese in the air and x/2 geese in the trees
    # 4 geese flew up from the trees, so there are now x/2 + 4 geese in the air forming a new V
    # The total number of geese in the new V is 12, so x/2 + 4 = 12
    # Solving for x, we get x = 16
    result = 16
    return result

print(solution())