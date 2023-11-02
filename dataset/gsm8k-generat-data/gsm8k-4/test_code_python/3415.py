def solution():
    """Jose owns a swimming pool. He charges $3 for kids and twice that amount for adults. If 8 kids and 10 adults swim in his swimming pool per day, how much money will he earn per week?"""
    # Define the price for kids and adults
    price_kids = 3
    price_adults = 2 * price_kids

    # Calculate the total earnings per day
    earnings_day = 8 * price_kids + 10 * price_adults

    # Calculate the total earnings per week
    earnings_week = 7 * earnings_day

    result = earnings_week
    return result

print(solution())