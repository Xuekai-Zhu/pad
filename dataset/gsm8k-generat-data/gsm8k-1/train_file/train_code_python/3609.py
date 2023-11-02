def solution():
    """Four people in a law firm are planning a party. Mary will buy a platter of pasta for $20 and a loaf of bread for $2. Elle and Andrea will split the cost for buying 4 cans of soda which cost $1.50 each, and chicken wings for $10. Joe will buy a cake that costs $5. How much more will Mary spend than the rest of the firm put together?"""
    mary_cost = 20 + 2
    elle_cost = andrea_cost = (4 * 1.5 + 10) / 2
    joe_cost = 5
    total_cost = mary_cost + elle_cost + andrea_cost + joe_cost
    cost_without_mary = total_cost - mary_cost
    difference = mary_cost - cost_without_mary
    result = difference
    return result

print(solution())