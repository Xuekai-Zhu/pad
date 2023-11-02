def solution():
    
    caramel_cost = 3
    candy_bar_price = 2 * caramel_cost
    cotton_candy_price = 0.5 * (4 * candy_bar_price)
    total_cost = (6 * candy_bar_price) + (3 * caramel_cost) + cotton_candy_price
    result = total_cost
    return result

print(solution())