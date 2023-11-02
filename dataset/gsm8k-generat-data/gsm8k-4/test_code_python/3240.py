def solution():
    """Leila spent $40 which is 1/4 of her money on a sweater. She was then left with $20 after spending the rest of her money on buying pieces of jewelry. How much more did Leila spend on jewelry than on the sweater?"""
    # Define the amount of money Leila had initially
    total_money = None

    # Calculate the amount of money spent on the sweater
    sweater_cost = 40

    # Calculate the remaining amount of money
    remaining_money = (1 - 1/4) * total_money

    # Calculate the amount of money spent on jewelry
    jewelry_cost = remaining_money - 20

    # Calculate the difference in cost
    difference = jewelry_cost - sweater_cost

    # return the result
    result = difference
    return result

print(solution())