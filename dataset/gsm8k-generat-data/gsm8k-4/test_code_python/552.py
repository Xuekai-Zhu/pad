def solution():
    """James paves a new parking lot.  It is 400 feet by 500 feet.  Only 80% of that is useable for parking.  It takes 10 square feet to park a car.  How many cars can be parked?"""
    # Define the dimensions of the parking lot
    length = 400
    width = 500

    # Calculate the total area of the parking lot
    total_area = length * width

    # Calculate the usable area of the parking lot
    usable_area = total_area * 0.8

    # Calculate the number of cars that can be parked
    cars_parked = int(usable_area / 10)

    # return the result
    result = cars_parked
    return result

print(solution())