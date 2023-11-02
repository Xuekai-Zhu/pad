def solution():
    
    dolls = 3
    clocks = 2
    glasses = 5
    doll_price = 5
    clock_price = 15
    glass_price = 4
    total_cost = 40
    total_profit = (dolls * doll_price) + (clocks * clock_price) + (glasses * glass_price) - total_cost
    result = total_profit
    return result

print(solution())