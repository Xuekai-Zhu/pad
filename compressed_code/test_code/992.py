def solution():
    
    total_peaches = 15
    friends_peaches = 10
    friends_price = 2
    relatives_peaches = 4
    relatives_price = 1.25
    remaining_peaches = 1
    friends_earnings = friends_peaches * friends_price
    relatives_earnings = relatives_peaches * relatives_price
    total_earnings = friends_earnings + relatives_earnings
    result = total_earnings
    return result

print(solution())