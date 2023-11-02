def solution():
    """Mary and her two friends agreed to evenly pay for the cost of 2 pounds of chicken. Mary's mother went to the grocery and bought the 2-pound chicken, 3 pounds of beef that cost $4 per pound, and a liter of oil that costs $1. If Mary's mother paid a total of $16 for the grocery, how much should Mary and her two friends pay each for the chicken?"""
    # Define the cost of beef and oil
    beef_cost = 3 * 4
    oil_cost = 1

    # Calculate the cost of the chicken
    total_cost = 16 - beef_cost - oil_cost
    chicken_cost = total_cost / 2

    # Calculate the cost of chicken for each person
    cost_per_person = chicken_cost / 3

    result = cost_per_person
    return result

print(solution())