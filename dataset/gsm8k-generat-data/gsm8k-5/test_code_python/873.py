def solution():
    apple_trees = 30  # There are 30 apple trees
    apple_yield = 150  # Each apple tree yields 150 kg of apples
    peach_trees = 45  # There are 45 peach trees
    peach_yield = 65  # Each peach tree yields 65 kg of fruit on average

    # Calculate the total mass of apples harvested
    total_apple_mass = apple_trees * apple_yield

    # Calculate the total mass of peaches harvested
    total_peach_mass = peach_trees * peach_yield

    # Calculate the total mass of fruit harvested
    total_fruit_mass = total_apple_mass + total_peach_mass
    result = total_fruit_mass
    return result

print(solution())