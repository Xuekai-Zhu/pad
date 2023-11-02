def solution():
    """There are 9 bicycles and 16 cars in the garage. How many wheels are there in the garage?"""
    # Define the number of wheels on each type of vehicle
    BICYCLE_WHEELS = 2
    CAR_WHEELS = 4

    # Calculate the total number of wheels on the bicycles
    bicycle_wheels = BICYCLE_WHEELS * 9

    # Calculate the total number of wheels on the cars
    car_wheels = CAR_WHEELS * 16

    # Calculate the total number of wheels in the garage
    total_wheels = bicycle_wheels + car_wheels

    # Display the total number of wheels
    result = total_wheels
    return result

print(solution())