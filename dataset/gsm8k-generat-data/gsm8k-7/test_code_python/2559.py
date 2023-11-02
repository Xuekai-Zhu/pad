def solution():
    selling_price_old_car = 1800
    remaining_cost_new_car = 2000
    cost_new_car = 2 * selling_price_old_car + remaining_cost_new_car
    cost_old_car = cost_new_car - selling_price_old_car - remaining_cost_new_car
    result = cost_old_car
    return result

print(solution())