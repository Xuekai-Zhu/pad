def solution():
    
    red_cars = 12
    green_cars = red_cars - 2
    blue_cars = green_cars * 3
    total_cars = 75
    yellow_cars = total_cars - red_cars - green_cars - blue_cars
    result = yellow_cars
    return result

print(solution())