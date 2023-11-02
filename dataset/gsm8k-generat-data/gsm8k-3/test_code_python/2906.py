def solution():
    """There are 20 bicycles, 10 cars and 5 motorcycles in the garage at Connor's house. How many wheels are there in the garage?"""
    # Define the number of wheels for each vehicle
    BICYCLE_WHEELS = 2
    CAR_WHEELS = 4
    MOTORCYCLE_WHEELS = 2

    # Define the number of each vehicle in the garage
    num_bicycles = 20
    num_cars = 10
    num_motorcycles = 5

    # Calculate the total number of wheels in the garage
    total_wheels = (num_bicycles * BICYCLE_WHEELS) + (num_cars * CAR_WHEELS) + (num_motorcycles * MOTORCYCLE_WHEELS)

    # Display the total number of wheels
    result = total_wheels
    return result

print(solution())