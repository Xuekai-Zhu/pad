def solution():
    
    oil_change_price = 20
    repair_price = 30
    car_wash_price = 5
    num_oil_changes = 5
    num_repairs = 10
    num_car_washes = 15
    total_earnings = (oil_change_price * num_oil_changes) + (repair_price * num_repairs) + (car_wash_price * num_car_washes)
    result = total_earnings
    return result

print(solution())