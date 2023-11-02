def solution():
    """Max has a collection of stamps in three colors: 20 red stamps, 80 blue stamps and 7 yellow ones. He is trying to sell the whole collection. He already sold 20 red stamps for the price of $1.1 for each stamp and 80 blue stamps for the price of $0.8 for each stamp. What price did he need to set for each yellow stamp to be able to earn the total of $100 from the whole sale?"""
    # Define the number and price of red and blue stamps already sold
    red_stamps_sold = 20
    red_stamps_price = 1.1
    blue_stamps_sold = 80
    blue_stamps_price = 0.8

    # Define the total number and price of yellow stamps
    yellow_stamps_total = 7
    yellow_stamps_price = 0

    # Define the total earnings from selling all stamps
    total_earnings = 100

    # Calculate the total earnings from selling red and blue stamps
    red_earnings = red_stamps_sold * red_stamps_price
    blue_earnings = blue_stamps_sold * blue_stamps_price
    total_earnings_remaining = total_earnings - red_earnings - blue_earnings

    # Calculate the price of each yellow stamp to earn the remaining total earnings
    if yellow_stamps_total > 0:
        yellow_stamps_price = total_earnings_remaining / yellow_stamps_total

    # return the result
    result = round(yellow_stamps_price, 2)
    return result

print(solution())