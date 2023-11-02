def solution():
    normal_ticket_price = 8
    normal_popcorn_price = normal_ticket_price - 3
    normal_drink_price = normal_popcorn_price + 1
    normal_candy_price = normal_drink_price / 2
    total_normal_price = normal_ticket_price + normal_popcorn_price + normal_drink_price + normal_candy_price
    bundle_price = 20
    result = total_normal_price - bundle_price
    
    return result

print(solution())