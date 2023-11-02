def solution():
    
    super_ticket_price = 20
    soda_price = 3
    popcorn_price = (soda_price - 2) / 1
    regular_price = popcorn_price - soda_price
    result = regular_price
    return result

print(solution())