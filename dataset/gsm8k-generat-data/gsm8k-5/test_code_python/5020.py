def solution():
    sales = 2500  # Alice sold $2500 worth of gadgets
    commission = 0.02 * sales  # Alice will receive a 2% commission on her sales
    total_earnings = 240 + commission  # Alice's total earnings for the month
    savings_rate = 0.1  # Alice saves 10% of her total earnings

    # Calculate the amount Alice will save this month
    savings = savings_rate * total_earnings
    result = savings
    return result

print(solution())