def solution():
    """Mary and her two friends agreed to evenly pay for the cost of 2 pounds of chicken. Mary's mother went to the grocery and bought the 2-pound chicken, 3 pounds of beef that cost $4 per pound, and a liter of oil that costs $1. If Mary's mother paid a total of $16 for the grocery, how much should Mary and her two friends pay each for the chicken?"""
    # Define the cost of the beef per pound and the cost of the oil
    BEEF_PRICE = 4
    OIL_PRICE = 1

    # Calculate the cost of the chicken
    total_cost = 16
    beef_cost = 3 * BEEF_PRICE
    oil_cost = OIL_PRICE
    chicken_cost = total_cost - beef_cost - oil_cost

    # Calculate the cost per person for the chicken
    num_people = 3 # Mary and her two friends
    cost_per_person = chicken_cost / num_people

    # Display the cost per person for the chicken
    result = cost_per_person
    return result

print(solution())