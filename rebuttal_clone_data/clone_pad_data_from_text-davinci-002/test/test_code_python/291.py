def solution():
     dirt_bikes = 3
     off_road_vehicles = 4
     cost_per_dirt_bike = 150
     cost_per_off_road_vehicle = 300
     registration_fee = 25
     total_cost = (dirt_bikes * cost_per_dirt_bike) + (off_road_vehicles * cost_per_off_road_vehicle) + (registration_fee * (dirt_bikes + off_road_vehicles))
     result = total_cost
     return result

print(solution())