def solution():
    total_vehicles = 50 + 40
    total_trucks = 50
    total_cars = 40
    percent_trucks_red = 50
    percent_trucks_black = 20
    percent_cars_white = 100
    percent_cars_red = 0
    percent_cars_black = 0
    
    percent_chance_white_truck = ((percent_trucks_red / 2) + percent_trucks_black) * (total_trucks / total_vehicles)
    result = percent_chance_white_truck
    
    return result

print(solution())