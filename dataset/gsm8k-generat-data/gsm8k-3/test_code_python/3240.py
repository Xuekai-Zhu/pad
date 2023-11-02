def solution():
    """Leila spent $40 which is 1/4 of her money on a sweater. She was then left with $20 after spending the rest of her money on buying pieces of jewelry. How much more did Leila spend on jewelry than on the sweater?"""
    # Set up the equation to solve for Leila's total money
    # Let x be Leila's total money
    # 40 = x/4 -> x = 160
    total_money = 160

    # Calculate how much Leila spent on jewelry
    jewelry_cost = total_money - 40 - 20

    # Calculate the difference between the cost of the jewelry and the sweater
    difference = jewelry_cost - 40

    # Display the difference
    result = difference
    return result

print(solution())