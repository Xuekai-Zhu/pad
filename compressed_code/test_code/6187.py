def solution():
    
    dirt_bike_quantity = 3
    dirt_bike_price = 150
    off_road_vehicle_quantity = 4
    off_road_vehicle_price = 300
    registration_fee = 25
    total_dirt_bike_cost = dirt_bike_quantity * dirt_bike_price
    total_off_road_vehicle_cost = off_road_vehicle_quantity * off_road_vehicle_price
    total_registration_cost = (dirt_bike_quantity + off_road_vehicle_quantity) * registration_fee
    total_cost = total_dirt_bike_cost + total_off_road_vehicle_cost + total_registration_cost
    result = total_cost
    return result

print(solution())