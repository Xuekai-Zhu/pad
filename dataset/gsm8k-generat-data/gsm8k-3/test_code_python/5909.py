def solution():
    """Jordan noticed that there are 2 cars in his driveway that each have 4 wheels.  There are 2 bikes and a trash can that each have 2 wheels.  There is also a tricycle and a pair of old roller skates.  How many wheels are there?"""
    # Calculate the total number of wheels for the cars
    car_wheels = 2 * 4

    # Calculate the total number of wheels for the bikes and trash can
    bike_trash_wheels = 2 * 2 + 2 * 2

    # Calculate the total number of wheels for the tricycle
    tricycle_wheels = 3

    # Calculate the total number of wheels for the roller skates
    roller_skates_wheels = 2 * 2

    # Calculate the total number of wheels
    total_wheels = car_wheels + bike_trash_wheels + tricycle_wheels + roller_skates_wheels

    # Display the total number of wheels
    result = total_wheels
    return result

print(solution())