def solution():
    plane_distance = 2000  # Distance between Arizona and New York by plane
    car_distance_increase = plane_distance * 0.4  # Distance increase when driving instead of flying
    total_car_distance = plane_distance + car_distance_increase  # Total distance when driving
    missouri_distance = total_car_distance / 2  # Missouri is midway between Arizona and New York

    # Calculate the distance between Missouri and New York
    distance_to_ny = total_car_distance - missouri_distance
    result = distance_to_ny
    return result

print(solution())