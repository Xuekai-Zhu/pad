def solution():
    """Bea and Dawn both have a lemonade stand. Bea sells her lemonade at 25 cents while Dawn sells hers at 28 cents. If Bea sold 10 glasses and Dawn sold 8 glasses, how much more money (in cents) did Bea earn than Dawn?"""
    # Define the price of Bea's lemonade and the number of glasses sold
    bea_price = 25
    bea_glasses = 10

    # Define the price of Dawn's lemonade and the number of glasses sold
    dawn_price = 28
    dawn_glasses = 8

    # Calculate the total earnings for each person
    bea_earnings = bea_glasses * bea_price
    dawn_earnings = dawn_glasses * dawn_price

    # Calculate the difference in earnings
    earnings_diff = bea_earnings - dawn_earnings

    # return the difference
    result = earnings_diff
    return result

print(solution())