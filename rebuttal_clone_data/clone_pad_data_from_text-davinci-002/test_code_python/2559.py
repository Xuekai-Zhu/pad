def solution():
    new_car_cost = 2 * old_car_cost
    money_from_old_car = 1800
    outstanding_debt = 2000
    old_car_cost = new_car_cost - outstanding_debt - money_from_old_car
    result = old_car_cost
    
    return result

print(solution())