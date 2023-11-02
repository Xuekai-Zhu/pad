def solution():
    # Define the prices of the sofa and armchairs
    sofa_price = 1250
    armchair_price = 425

    # Calculate the total cost of the sofa and armchairs
    sofa_and_armchair_cost = 2 * armchair_price + sofa_price

    # Calculate the price of the coffee table by subtracting the sofa and armchair cost from the total invoice amount
    coffee_table_price = 2430 - sofa_and_armchair_cost
    result = coffee_table_price
    return result

print(solution())