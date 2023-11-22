def solution():
    
    # Define the prices of gingerbread and apple pie
    gingerbread_price = 6
    apple_pie_price = 15

    # Calculate the prices of gingerbread and apple pie sold on Saturday
    saturday_price = 10 * gingerbread_price + 4
    saturday_apple_pie_price = 15 * apple_pie_price

    # Calculate the prices of gingerbread and apple pie sold on Sunday
    sunday_price = saturday_price + 5
    sunday_apple_pie_price = 15 * apple_pie_price

    # Calculate the total earnings for two days
    total_earnings = saturday_earnings + sunday_earnings

    # return the result
    result = total_earnings
    return result

print(solution())