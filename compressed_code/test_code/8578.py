def solution():
    
    distance_first_package = 10
    distance_second_package = 28
    distance_third_package = distance_second_package / 2
    total_distance = distance_first_package + distance_second_package + distance_third_package
    payment = 104
    payment_per_mile = payment / total_distance
    result = payment_per_mile
    return result

print(solution())