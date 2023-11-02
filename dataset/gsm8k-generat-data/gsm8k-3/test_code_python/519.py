def solution():
    """Harrison buys a regular croissant on Saturdays for $3.50 and an almond croissant for $5.50 on Sundays.  How much does he spend on croissants in a year?"""
    # Define the cost of a regular croissant and an almond croissant
    REGULAR_PRICE = 3.5
    ALMOND_PRICE = 5.5

    # Calculate the number of croissants Harrison buys in a year
    regular_croissants = 52
    almond_croissants = 52

    # Calculate the total cost for regular croissants
    regular_cost = regular_croissants * REGULAR_PRICE

    # Calculate the total cost for almond croissants
    almond_cost = almond_croissants * ALMOND_PRICE

    # Calculate the total cost for all croissants in a year
    total_cost = regular_cost + almond_cost

    # Display the total cost
    result = total_cost
    return result

print(solution())