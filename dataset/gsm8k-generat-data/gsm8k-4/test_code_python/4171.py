def solution():
    """William washes cars as a side job. He typically spends 4 minutes washing a car’s windows, 7 minutes washing the car body, 4 minutes cleaning the tires, and 9 minutes waxing the car. This morning he washed 2 normal cars and one big SUV, which took twice as long as a normal car. How many minutes did William spend washing all the vehicles?"""
    # Define the time taken to wash each part of a normal car
    windows_time = 4
    body_time = 7
    tire_time = 4
    wax_time = 9

    # Define the number of normal cars and the time taken to wash each
    normal_cars = 2
    normal_car_time = windows_time + body_time + tire_time + wax_time

    # Define the time taken to wash the big SUV
    suv_time = normal_car_time * 2

    # Calculate the total time taken to wash all the vehicles
    total_time = (normal_cars * normal_car_time) + suv_time

    # return the result
    result = total_time
    return result

print(solution())