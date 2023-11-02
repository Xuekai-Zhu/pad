def solution():
    """Leila bought a living room set consisting of a sofa worth $1,250, 2 armchairs costing $425 each and a coffee table. The total amount of the invoice is $2,430. What is the price of the coffee table?"""
    sofa_price = 1250
    armchair_price = 425
    total_price = 2430
    num_armchairs = 2
    sofa_and_armchair_price = sofa_price + num_armchairs * armchair_price
    coffee_table_price = total_price - sofa_and_armchair_price
    result = coffee_table_price
    return result

print(solution())