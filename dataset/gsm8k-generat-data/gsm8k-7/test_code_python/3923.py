def solution():
    apple_price = 1.25
    bike_cost = 80
    repair_cost = bike_cost * 0.25
    total_profit = (bike_cost + repair_cost) / 0.8  # 1/5 of the money earned remains
    num_apples = total_profit / apple_price
    result = num_apples
    return result

print(solution())