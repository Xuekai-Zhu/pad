def solution():
    # Define the number and values of stamps already sold
    red_sold = 20
    blue_sold = 80
    red_price = 1.1
    blue_price = 0.8

    # Calculate the total earned from selling red and blue stamps
    red_earnings = red_sold * red_price
    blue_earnings = blue_sold * blue_price
    total_earnings = red_earnings + blue_earnings

    # Calculate the earnings needed from selling yellow stamps
    yellow_stamps = 7
    yellow_earnings = 100 - total_earnings
    yellow_price = yellow_earnings / yellow_stamps
    result = yellow_price
    return result

print(solution())