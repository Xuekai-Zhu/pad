def solution():
    
    jude_bottle_caps = 100
    truck_price = 6
    car_price = 5
    truck_quantity = 10
    total_truck_cost = truck_quantity * truck_price
    remaining_bottle_caps = jude_bottle_caps - total_truck_cost
    car_quantity = int((remaining_bottle_caps * 0.75) / car_price)
    total_quantity = truck_quantity + car_quantity
    result = total_quantity
    return result

print(solution())