def solution():
     car_wash_time = 10
     oil_change_time = 15
     tire_change_time = 30
     number_of_car_washes = 9
     number_of_oil_changes = 6
     number_of_tire_changes = 2
     
     total_time = (car_wash_time * number_of_car_washes) + (oil_change_time * number_of_oil_changes) + (tire_change_time * number_of_tire_changes)
     total_hours = total_time / 60
     
     result = total_hours
     
     return result

print(solution())