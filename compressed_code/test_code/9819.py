def solution():
    
    oil_change_cost = 20
    repair_cost = 30
    car_wash_cost = 5
    num_oil_changes = 5
    num_repairs = 10
    num_car_washes = 15
    total_earnings = (oil_change_cost * num_oil_changes) + (repair_cost * num_repairs) + (car_wash_cost * num_car_washes)
    result = total_earnings
    return result

print(solution())