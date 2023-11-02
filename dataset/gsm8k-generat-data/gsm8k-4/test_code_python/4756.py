def solution():
    """Sasha heard that planting trees helps to reduce the local temperature. For each tree planted, the temperature drops .1 degree. A tree costs $6 to plant. If she got the local temperature to drop from 80 to 78.2, how much did it cost to plant the trees?"""
    
    # Calculate the temperature decrease
    temperature_decrease = 80 - 78.2

    # Calculate the number of trees needed to achieve the temperature decrease
    trees_needed = temperature_decrease / 0.1

    # Calculate the cost of planting the trees
    trees_cost = trees_needed * 6

    # Return the result
    result = trees_cost
    return result

print(solution())