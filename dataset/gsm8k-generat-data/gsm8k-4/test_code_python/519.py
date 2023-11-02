def solution():
    """Harrison buys a regular croissant on Saturdays for $3.50 and an almond croissant for $5.50 on Sundays. How much does he spend on croissants in a year?"""
    # Define the cost of a regular croissant and an almond croissant
    regular_croissant_cost = 3.5
    almond_croissant_cost = 5.5

    # Calculate the total cost of croissants in a week
    weekly_cost = regular_croissant_cost + almond_croissant_cost

    # Calculate the total cost of croissants in a year (assuming 52 weeks in a year)
    yearly_cost = weekly_cost * 52

    # return the result
    result = yearly_cost
    return result

print(solution())