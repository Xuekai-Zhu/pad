def solution():
    """William washes cars as a side job. He typically spends 4 minutes washing a car’s windows, 7 minutes washing the car body, 4 minutes cleaning the tires, and 9 minutes waxing the car. This morning he washed 2 normal cars and one big SUV, which took twice as long as a normal car. How many minutes did William spend washing all the vehicles?"""
    # Define the time William spends washing various parts of a normal car
    WINDOWS_TIME = 4
    BODY_TIME = 7
    TIRES_TIME = 4
    WAXING_TIME = 9

    # Calculate the total time William spends washing a normal car
    normal_car_time = WINDOWS_TIME + BODY_TIME + TIRES_TIME + WAXING_TIME

    # Calculate the total time William spends washing a big SUV
    big_suv_time = normal_car_time * 2

    # Calculate the total time William spends washing all the vehicles
    total_time = (normal_car_time * 2) + big_suv_time

    # Display the total time spent washing all the vehicles
    result = total_time
    return result

print(solution())