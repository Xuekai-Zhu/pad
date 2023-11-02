def solution():
    sofa_price = 1250
    armchair_price = 425
    num_armchairs = 2
    total_invoice = 2430

    # Calculate the total cost of the sofa and armchairs
    total_sofa_and_armchair_cost = (sofa_price + (num_armchairs * armchair_price))

    # Calculate the price of the coffee table
    coffee_table_price = total_invoice - total_sofa_and_armchair_cost
    result = coffee_table_price
    return result

print(solution())