def solution():
    tree_height = 100  # The tree was 100 meters tall at the end of 2017
    growth_rate = 1.1  # The tree grows 10% more each year
    years = 2  # We want to know how long the tree has grown from 2017 until the end of 2019

    # Calculate the tree's height at the end of 2019
    final_height = tree_height * (growth_rate ** years)

    # Calculate how much the tree has grown from 2017 until the end of 2019
    growth = final_height - tree_height
    result = growth
    return result

print(solution())