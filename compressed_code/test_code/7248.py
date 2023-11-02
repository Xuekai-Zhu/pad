def solution():
    
    total_trucks = 50
    red_trucks_percent = 50
    black_trucks_percent = 20
    white_trucks_percent = 100 - red_trucks_percent - black_trucks_percent
    white_trucks = total_trucks * white_trucks_percent / 100
    total_cars = 40
    total_vehicles = total_trucks + total_cars
    probability = white_trucks / total_vehicles * 100
    result = round(probability)
    
    return result

print(solution())