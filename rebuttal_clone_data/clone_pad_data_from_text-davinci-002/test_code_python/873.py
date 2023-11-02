def solution():
    apple_trees = 30
    average_apple_yield = 150
    peach_trees = 45
    average_peach_yield = 65
    total_apple_yield = apple_trees * average_apple_yield
    total_peach_yield = peach_trees * average_peach_yield
    total_yield = total_apple_yield + total_peach_yield
    result = total_yield
    return result

print(solution())