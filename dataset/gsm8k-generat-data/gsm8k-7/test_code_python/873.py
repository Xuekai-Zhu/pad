def solution():
    num_apple_trees = 30
    apple_yield_per_tree = 150  # in kg

    num_peach_trees = 45
    peach_yield_per_tree = 65  # in kg

    # Calculate the total mass of apples harvested
    total_apple_yield = num_apple_trees * apple_yield_per_tree

    # Calculate the total mass of peaches harvested
    total_peach_yield = num_peach_trees * peach_yield_per_tree

    # Calculate the total mass of fruit harvested
    total_yield = total_apple_yield + total_peach_yield
    result = total_yield
    return result

print(solution())