def solution():
    # Calculate the number of rolls of wrapping paper needed for the shirt boxes
    shirt_rolls = 20 / 5  # 5 shirt boxes can be wrapped with one roll of paper

    # Calculate the number of rolls of wrapping paper needed for the XL boxes
    xl_rolls = 12 / 3  # 3 XL boxes can be wrapped with one roll of paper

    # Total number of rolls needed
    total_rolls = shirt_rolls + xl_rolls

    # Cost per roll of wrapping paper
    cost_per_roll = 4.00

    # Calculate the total cost
    total_cost = total_rolls * cost_per_roll
    result = total_cost
    return result

print(solution())