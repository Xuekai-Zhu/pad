def solution():
    cost_caramel = 3
    price_candy_bar = cost_caramel * 2
    price_cotton_candy = price_candy_bar * 4
    total_cost = (6 * price_candy_bar) + (3 * cost_caramel) + price_cotton_candy
    result = total_cost
    
    return result

print(solution())