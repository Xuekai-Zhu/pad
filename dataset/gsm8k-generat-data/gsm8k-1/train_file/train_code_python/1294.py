def solution():
    """Lilia has 15 peaches. She sold 10 peaches to her friends for $2 each, while 4 other peaches were sold to her relatives for $1.25 each, and she left the other one for herself. How much did she earn after selling 14 peaches?"""
    total_peaches = 15
    peaches_sold = 14
    friend_price = 2
    relative_price = 1.25
    peaches_to_friends = 10
    peaches_to_relatives = 4
    earnings_from_friends = peaches_to_friends * friend_price
    earnings_from_relatives = peaches_to_relatives * relative_price
    total_earnings = earnings_from_friends + earnings_from_relatives
    result = total_earnings
    
    return result

print(solution())