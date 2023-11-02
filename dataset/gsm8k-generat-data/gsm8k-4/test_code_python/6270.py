def solution():
    """There are 9 bicycles and 16 cars in the garage. How many wheels are there in the garage?"""
    # Define the number of wheels on bicycles and cars
    bicycle_wheels = 2
    car_wheels = 4

    # Calculate the total number of wheels on bicycles and cars
    total_wheels = (9 * bicycle_wheels) + (16 * car_wheels)

    # Return the result
    result = total_wheels
    return result

print(solution())