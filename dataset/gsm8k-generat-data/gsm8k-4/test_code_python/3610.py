def solution():
    """Four people in a law firm are planning a party. Mary will buy a platter of pasta for $20 and a loaf of bread for $2. Elle and Andrea will split the cost for buying 4 cans of soda which cost $1.50 each, and chicken wings for $10. Joe will buy a cake that costs $5. How much more will Mary spend than the rest of the firm put together?"""
    # Calculate the cost Mary will spend on food
    mary_cost = 20 + 2

    # Calculate the cost Elle and Andrea will spend on drinks and chicken wings
    drink_cost = 4 * 1.5
    chicken_wings_cost = 10
    elle_andrea_cost = (drink_cost + chicken_wings_cost) / 2

    # Calculate the cost Joe will spend on the cake
    joe_cost = 5

    # Calculate the total cost of the party
    total_cost = mary_cost + elle_andrea_cost + joe_cost

    # Calculate the cost the rest of the firm (excluding Mary) put together
    rest_cost = total_cost - mary_cost

    # Calculate the difference in cost between Mary and the rest of the firm
    difference = mary_cost - rest_cost

    # return the result
    result = difference
    return result

print(solution())