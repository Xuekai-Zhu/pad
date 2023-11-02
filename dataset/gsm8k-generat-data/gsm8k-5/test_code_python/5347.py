def solution():
    cola_price = 3
    juice_price = 1.5
    water_price = 1

    total_cola_sales = cola_price * 15
    total_juice_sales = juice_price * 12
    total_water_sales = water_price * 25

    # Calculate the total earning
    total_earning = total_cola_sales + total_juice_sales + total_water_sales
    result = total_earning
    return result

print(solution())