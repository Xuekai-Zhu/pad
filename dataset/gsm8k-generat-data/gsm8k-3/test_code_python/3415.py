def solution():
    """Jose owns a swimming pool. He charges $3 for kids and twice that amount for adults. If 8 kids and 10 adults swim in his swimming pool per day, how much money will he earn per week?"""
    # Define the price for kids and adults
    KID_PRICE = 3
    ADULT_PRICE = KID_PRICE * 2

    # Define the number of kids and adults per day
    kids_per_day = 8
    adults_per_day = 10

    # Calculate the earnings per day
    daily_earnings = kids_per_day * KID_PRICE + adults_per_day * ADULT_PRICE

    # Calculate the earnings per week
    weekly_earnings = daily_earnings * 7

    # Display the weekly earnings
    result = weekly_earnings
    return result

print(solution())