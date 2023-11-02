def solution():
    # Find the total number of trees planted by Mary
    total_trees = 6 * 2  # Mary planted 2 trees for each apple she didn't eat
    # Since Mary planted the remaining apples, she must have eaten all the apples she bought except the planted ones
    eaten_apples = 6 - (total_trees / 2)
    result = eaten_apples
    return result

print(solution())