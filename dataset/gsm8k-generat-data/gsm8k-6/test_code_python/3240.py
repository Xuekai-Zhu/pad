def solution():
    # Calculate Leila's total amount of money
    total_money = 40 * 4  # she spent 1/4 of her money on the sweater, so 40 is 1/4 of her money

    # Calculate how much she spent on jewelry
    jewelry_spending = total_money - 40 - 20  # she spent the rest of her money on jewelry after buying the sweater for $40

    # Calculate the difference in spending between the sweater and jewelry
    difference = jewelry_spending - 40

    result = difference
    return result

print(solution())