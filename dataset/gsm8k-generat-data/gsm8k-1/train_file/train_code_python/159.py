def solution():
    """John throws a block party and splits the cost with 3 other people. They buy 100 pounds of burgers at $3 per pound. They also buy $80 of condiments and propane to cook everything. John also buys all the alcohol which costs $200. How much did John spend altogether?"""
    burger_cost = 100 * 3
    condiment_cost = 80
    alcohol_cost = 200
    total_cost = burger_cost + condiment_cost + alcohol_cost
    john_share = total_cost / 4
    result = john_share
    return result

print(solution())