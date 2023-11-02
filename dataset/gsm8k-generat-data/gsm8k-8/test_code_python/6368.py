def solution():
    # Calculate Nigella's commission for the month
    commission = 8000 - 3000
    total_sale = commission / 0.02

    # Set up equations for the house prices
    # Let x be the cost of House A
    # House B costs three times as much as House A, so its cost is 3x
    # House C cost twice as much as House A minus $110,000, so its cost is 2(x - 110000)
    # The total sale is the sum of the prices of the three houses, so:
    # x + 3x + 2(x - 110000) = total_sale

    # Simplify the equation and solve for x
    x = (total_sale + 220000) / 6
    result = x
    return result

print(solution())