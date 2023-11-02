def solution():
    current_car_cost = 20
    new_car_cost = 30
    months_per_year = 12
    total_cost_current_car = current_car_cost * months_per_year
    total_cost_new_car = new_car_cost * months_per_year
    result = total_cost_new_car - total_cost_current_car
    return result

print(solution())