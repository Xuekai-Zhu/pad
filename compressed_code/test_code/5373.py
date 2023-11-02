def solution():
    
    coal_cars = 6
    iron_cars = 12
    wood_cars = 2
    miles_per_station = 6
    time_per_station = 25
    max_coal_deposit = 2
    max_iron_deposit = 3
    max_wood_deposit = 1

    
    coal_stations = (coal_cars // max_coal_deposit) + (coal_cars % max_coal_deposit > 0)
    iron_stations = (iron_cars // max_iron_deposit) + (iron_cars % max_iron_deposit > 0)
    wood_stations = (wood_cars // max_wood_deposit) + (wood_cars % max_wood_deposit > 0)
    total_stations = max(coal_stations, iron_stations, wood_stations)

    
    total_time = total_stations * time_per_station

    result = total_time
    return result

print(solution())