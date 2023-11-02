def solution():
    # Calculate the height of the tree after 4 months (16 weeks)
    growth_per_week = 2 # the tree grows at a rate of 2 feet per week
    total_growth = growth_per_week * 16 # multiply the weeks in 4 months by the growth rate
    tree_height = 10 + total_growth # add the initial height of the tree to the total growth
    result = tree_height
    return result

print(solution())