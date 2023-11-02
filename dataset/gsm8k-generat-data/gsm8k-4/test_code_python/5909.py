def solution():
    """Jordan noticed that there are 2 cars in his driveway that each have 4 wheels. There are 2 bikes and a trash can that each have 2 wheels. There is also a tricycle and a pair of old roller skates. How many wheels are there?"""
    # Define the number of wheels per item
    car_wheels = 4
    bike_wheels = 2
    trash_can_wheels = 2
    tricycle_wheels = 3
    roller_skate_wheels = 4

    # Calculate the total number of wheels
    total_wheels = 2 * car_wheels + 2 * bike_wheels + trash_can_wheels + tricycle_wheels + 2 * roller_skate_wheels

    result = total_wheels
    return result

print(solution())