def solution():
    
    truck_tire_price = 60
    car_tire_price = 40
    thursday_truck_tires = 6
    thursday_car_tires = 4
    friday_car_tires = 12
    friday_truck_tires = 0
    friday_car_tires = 0
    thursday_revenue = (truck_tire_price * thursday_truck_tires) + (car_tire_price * thursday_car_tires)
    friday_revenue = (car_tire_price * friday_car_tires)
    total_revenue = (truck_tire_price * thursday_truck_tires) + (car_tire_price * thursday_car_tires)
    difference = friday_revenue - total_revenue
    result = difference
    return result

print(solution())