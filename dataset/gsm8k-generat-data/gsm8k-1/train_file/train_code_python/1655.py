def solution():
    """Holly wants to plant a wall of privacy trees along her fence line. Her fence is 25 yards long. At maturity, the trees she wants to plant will measure 1.5 feet wide. Right now, these trees are on sale for $8.00 apiece. How much will it cost her to plant a row of the trees to run the length of her fence?"""
    fence_length = 25 # yards
    tree_width = 1.5 # feet
    tree_cost = 8 # dollars
    feet_per_yard = 3
    trees_needed = round(fence_length * feet_per_yard / tree_width)
    total_cost = trees_needed * tree_cost
    result = total_cost
    return result

print(solution())