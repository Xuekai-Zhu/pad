def solution():
    """Leila bought a living room set consisting of a sofa worth $1,250, 2 armchairs costing $425 each and a coffee table. The total amount of the invoice is $2,430. What is the price of the coffee table?"""
    # Define the prices of the sofa and armchairs
    sofa_price = 1250
    armchair_price = 425

    # Calculate the total amount paid for the sofa and armchairs
    sofa_armchair_total = sofa_price + (2 * armchair_price)

    # Calculate the price of the coffee table
    coffee_table_price = 2430 - sofa_armchair_total

    # return the result
    result = coffee_table_price
    return result

print(solution())