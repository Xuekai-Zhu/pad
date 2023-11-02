def solution():
    """Kurt's old refrigerator cost $0.85 a day in electricity. He recently bought a new energy-efficient refrigerator that only cost $0.45 a day in electricity. How much money does Kurt save in a 30-day month with his new refrigerator?"""
    # Define the daily cost of electricity for the old and new refrigerators
    old_cost = 0.85
    new_cost = 0.45

    # Calculate the difference in cost per day
    cost_difference = old_cost - new_cost

    # Calculate the total savings in a 30-day month
    savings = cost_difference * 30

    # return the result
    result = savings
    return result

print(solution())