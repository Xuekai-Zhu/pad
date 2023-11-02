def solution():
    """Four people in a law firm are planning a party. Mary will buy a platter of pasta for $20 and a loaf of bread for $2. Elle and Andrea will split the cost for buying 4 cans of soda which cost $1.50 each, and chicken wings for $10. Joe will buy a cake that costs $5. How much more will Mary spend than the rest of the firm put together?"""
    mary_total_cost = 20 + 2
    elle_andrea_soda_cost = 4 * 1.5 / 2
    joe_cake_cost = 5
    total_cost_excluding_mary = elle_andrea_soda_cost + joe_cake_cost + 10
    difference = mary_total_cost - total_cost_excluding_mary
    result = difference
    return result

print(solution())