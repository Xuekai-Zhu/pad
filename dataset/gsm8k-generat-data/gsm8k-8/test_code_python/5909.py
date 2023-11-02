def solution():
    # Calculate the total number of wheels on cars
    car_wheels = 2 * 4

    # Calculate the total number of wheels on bikes and trash can
    bike_trash_wheels = 2 * 2 + 2

    # Calculate the total number of wheels on tricycle and roller skates
    tri_skates_wheels = 3 + 4

    # Add up all the wheels to get the total
    total_wheels = car_wheels + bike_trash_wheels + tri_skates_wheels
    result = total_wheels
    return result

print(solution())