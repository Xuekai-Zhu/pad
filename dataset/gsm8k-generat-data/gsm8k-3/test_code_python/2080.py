def solution():
    """A hairstylist charges $5 for a normal haircut, $6 for a special haircut, and $8 for a trendy haircut. If he cuts 5 normal haircuts, 3 special haircuts, and 2 trendy haircuts per day, how much money does he earn per week?"""
    # Define the prices for each type of haircut
    NORMAL_PRICE = 5
    SPECIAL_PRICE = 6
    TRENDY_PRICE = 8

    # Calculate the earnings for each type of haircut per day
    normal_earnings = NORMAL_PRICE * 5
    special_earnings = SPECIAL_PRICE * 3
    trendy_earnings = TRENDY_PRICE * 2

    # Calculate the total earnings per day
    total_earnings_per_day = normal_earnings + special_earnings + trendy_earnings

    # Calculate the total earnings per week
    total_earnings_per_week = total_earnings_per_day * 7

    # Display the total earnings per week
    result = total_earnings_per_week
    return result

print(solution())