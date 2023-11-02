def solution():
    num_peaches = 15

    # Calculate the total earnings from selling 10 peaches to friends
    num_friends_peaches = 10
    friends_price = 2
    friends_total_earnings = num_friends_peaches * friends_price

    # Calculate the total earnings from selling 4 peaches to relatives
    num_relatives_peaches = 4
    relatives_price = 1.25
    relatives_total_earnings = num_relatives_peaches * relatives_price

    # Calculate the total earnings from selling 14 peaches
    total_earnings = friends_total_earnings + relatives_total_earnings

    result = total_earnings
    return result

print(solution())