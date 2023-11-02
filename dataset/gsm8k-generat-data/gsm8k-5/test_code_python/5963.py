def solution():
    sofa_price = 1250
    armchair_price = 425
    total_price = 2430
    num_armchairs = 2

    # Calculate the total cost of the sofa and armchairs
    sofa_armchair_price = sofa_price + armchair_price*num_armchairs

    # Calculate the price of the coffee table
    coffee_table_price = total_price - sofa_armchair_price
    result = coffee_table_price
    return result

print(solution())