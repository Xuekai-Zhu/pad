def solution():
    """Bea and Dawn both have a lemonade stand. Bea sells her lemonade at 25 cents while Dawn sells hers at 28 cents. If Bea sold 10 glasses and Dawn sold 8 glasses, how much more money (in cents) did Bea earn than Dawn?"""
    # Define the price of lemonade for each person and the number of glasses sold
    BEA_PRICE = 25
    DAWN_PRICE = 28
    BEA_GLASSES = 10
    DAWN_GLASSES = 8

    # Calculate the amount of money earned by each person
    bea_money = BEA_PRICE * BEA_GLASSES
    dawn_money = DAWN_PRICE * DAWN_GLASSES

    # Calculate the difference in money earned
    difference = bea_money - dawn_money

    # Display the difference in money earned
    result = difference
    return result

print(solution())