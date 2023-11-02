def solution():
    """Sasha heard that planting trees helps to reduce the local temperature. For each tree planted, the temperature drops .1 degree. A tree costs $6 to plant. If she got the local temperature to drop from 80 to 78.2, how much did it cost to plant the trees?"""
    # Calculate the temperature difference
    temp_diff = 80 - 78.2

    # Calculate the number of trees needed to achieve the temperature difference
    trees_needed = temp_diff / 0.1

    # Calculate the total cost of planting the trees
    total_cost = trees_needed * 6

    # Display the total cost
    result = total_cost
    return result

print(solution())