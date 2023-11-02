def solution():
    num_bicycles = 9
    num_cars = 16

    # Calculate the total number of bicycle wheels
    bicycle_wheels = num_bicycles * 2

    # Calculate the total number of car wheels
    car_wheels = num_cars * 4

    # Calculate the total number of wheels in the garage
    total_wheels = bicycle_wheels + car_wheels
    result = total_wheels
    return result

print(solution())