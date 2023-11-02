def solution():
    arizona_ny_distance = 2000
    increase_percentage = 0.4
    car_distance = arizona_ny_distance + (arizona_ny_distance * increase_percentage)
    missouri_distance = car_distance / 2
    distance_to_ny = car_distance - missouri_distance
    result = distance_to_ny
    return result

print(solution())