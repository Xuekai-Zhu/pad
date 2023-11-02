def solution():
    # Calculate the time to wash one normal car
    normal_car_time = 4 + 7 + 4 + 9  # Total time spent on a normal car

    # Calculate the time to wash the SUV
    suv_time = 2 * normal_car_time  # The SUV takes twice as long as a normal car

    # Calculate the total time spent
    total_time = (2 * normal_car_time) + suv_time  # William washed 2 normal cars and 1 SUV

    result = total_time
    return result

print(solution())