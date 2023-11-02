def solution():
    # Define the prices of haircuts
    normal_price = 5
    special_price = 6
    trendy_price = 8

    # Calculate the daily earnings from each type of haircut
    normal_earnings = normal_price * 5
    special_earnings = special_price * 3
    trendy_earnings = trendy_price * 2

    # Calculate the total daily earnings
    total_earnings = normal_earnings + special_earnings + trendy_earnings

    # Calculate the weekly earnings
    weekly_earnings = total_earnings * 7

    result = weekly_earnings
    return result

print(solution())