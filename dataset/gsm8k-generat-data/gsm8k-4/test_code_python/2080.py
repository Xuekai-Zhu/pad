def solution():
    """A hairstylist charges $5 for a normal haircut, $6 for a special haircut, and $8 for a trendy haircut. If he cuts 5 normal haircuts, 3 special haircuts, and 2 trendy haircuts per day, how much money does he earn per week?"""
    # Define the prices for each type of haircut
    NORMAL_PRICE = 5
    SPECIAL_PRICE = 6
    TRENDY_PRICE = 8

    # Define the number of haircuts per day
    NORMAL_HAIRCUTS = 5
    SPECIAL_HAIRCUTS = 3
    TRENDY_HAIRCUTS = 2

    # Calculate the earnings per day
    earnings_per_day = (NORMAL_PRICE * NORMAL_HAIRCUTS) + (SPECIAL_PRICE * SPECIAL_HAIRCUTS) + (TRENDY_PRICE * TRENDY_HAIRCUTS)

    # Calculate the earnings per week
    earnings_per_week = earnings_per_day * 7

    # return the result
    result = earnings_per_week
    return result

print(solution())