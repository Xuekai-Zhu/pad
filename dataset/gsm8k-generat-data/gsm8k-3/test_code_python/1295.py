def solution():
    """Lilia has 15 peaches. She sold 10 peaches to her friends for $2 each, while 4 other peaches were sold to her relatives for $1.25 each, and she left the other one for herself. How much did she earn after selling 14 peaches?"""
    # Define the number of peaches sold and their respective prices
    friends_peaches = 10
    friends_price = 2
    relatives_peaches = 4
    relatives_price = 1.25

    # Calculate the total earnings from selling to her friends and relatives
    total_earnings = (friends_peaches * friends_price) + (relatives_peaches * relatives_price)

    # Calculate the remaining number of peaches and earnings
    remaining_peaches = 15 - 1 - friends_peaches - relatives_peaches
    remaining_earnings = remaining_peaches * friends_price

    # Calculate the total earnings after selling 14 peaches
    total_earnings_14 = total_earnings + remaining_earnings

    # Display the total earnings after selling 14 peaches
    result = total_earnings_14
    return result

print(solution())