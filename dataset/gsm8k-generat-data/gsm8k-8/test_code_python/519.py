def solution():
    # Define the cost of one regular croissant and one almond croissant
    regular_cost = 3.5
    almond_cost = 5.5

    # Calculate the total cost of croissants for one weekend (Saturday and Sunday)
    weekend_cost = regular_cost + almond_cost

    # Calculate the total cost of croissants for one year (52 weeks)
    yearly_cost = weekend_cost * 52

    result = yearly_cost
    return result

print(solution())