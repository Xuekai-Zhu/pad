def solution():
    """Lilia has 15 peaches. She sold 10 peaches to her friends for $2 each, while 4 other peaches were sold to her relatives for $1.25 each, and she left the other one for herself. How much did she earn after selling 14 peaches?"""
    # Define the initial number of peaches and the prices
    peaches = 15
    FRIEND_PRICE = 2
    RELATIVE_PRICE = 1.25

    # Calculate the earnings from selling peaches to friends
    friends_earnings = 10 * FRIEND_PRICE

    # Calculate the earnings from selling peaches to relatives
    relatives_earnings = 4 * RELATIVE_PRICE

    # Calculate the total earnings and the remaining peach
    total_earnings = friends_earnings + relatives_earnings
    remaining_peaches = peaches - 14

    # Calculate the earnings from the remaining peach
    self_earnings = remaining_peaches * FRIEND_PRICE

    # Add the earnings to the total
    total_earnings += self_earnings

    # return the result
    result = total_earnings
    return result

print(solution())