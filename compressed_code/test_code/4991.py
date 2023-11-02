def solution():
    
    bun_price = 0.1
    milk_price = 2
    carton_price = 3 * milk_price
    bun_total = 10 * bun_price
    milk_total = 2 * milk_price
    carton_total = carton_price
    total_cost = bun_total + milk_total + carton_total
    result = total_cost
    return result

print(solution())