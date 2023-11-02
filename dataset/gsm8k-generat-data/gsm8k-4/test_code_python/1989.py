def solution():
    """Yulia was able to net $44 in profit this week. Her lemonade stand made a gross revenue of $47 this week. She was also able to babysit and made $31. However, her lemonade stand is expensive to run because she needs to buy lemons, sugar, and sunscreen. How much did she spend to operate her lemonade stand, in dollars?"""
    # Define the gross revenue and the babysitting earnings
    gross_revenue = 47
    babysitting_earnings = 31

    # Calculate the total earnings
    total_earnings = gross_revenue + babysitting_earnings

    # Calculate the net profit
    net_profit = 44

    # Calculate the expenses
    expenses = total_earnings - net_profit

    result = expenses
    return result

print(solution())