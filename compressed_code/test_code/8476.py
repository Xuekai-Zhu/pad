def solution():
    
    ticket_price = 8
    popcorn_price = 5
    drink_price = 6
    candy_price = 3
    normal_price = ticket_price + popcorn_price + drink_price + candy_price
    deal_price = 20
    savings = normal_price - deal_price
    result = savings
    return result

print(solution())