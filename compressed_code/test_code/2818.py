def solution():
    
    gustran_total_price = 45 + 22 + 30
    barbara_total_price = 40 + 30 + 28
    fancy_total_price = 30 + 34 + 20

    cheapest_price = min(gustran_total_price, barbara_total_price, fancy_total_price)

    result = cheapest_price
    return result

print(solution())