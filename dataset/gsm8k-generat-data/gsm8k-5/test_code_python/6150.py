def solution():
    growth_rate = 50  # The tree grows 50 centimeters every 2 weeks
    initial_height = 200  # The tree is currently 2 meters (200 centimeters) tall
    total_growth = growth_rate * 8  # There are 8 two-week intervals in 4 months
    final_height = initial_height + total_growth  # Calculate the final height of the tree

    result = final_height
    return result

print(solution())