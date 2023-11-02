def solution():
    # Calculate the total cost of the sofa and armchairs
    total_sofa_armchairs = 1250 + 2*425  # sofa worth $1,250, 2 armchairs costing $425 each

    # Calculate the price of the coffee table
    price_coffee_table = 2430 - total_sofa_armchairs  # The total amount of the invoice is $2,430

    result = price_coffee_table
    return result

print(solution())