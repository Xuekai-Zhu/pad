def solution():
    """James paves a new parking lot.  It is 400 feet by 500 feet.  Only 80% of that is useable for parking.  It takes 10 square feet to park a car.  How many cars can be parked?"""
    # Define the dimensions of the parking lot
    length = 400
    width = 500

    # Calculate the total area of the parking lot and the area available for parking
    total_area = length * width
    usable_area = total_area * 0.8

    # Calculate the number of cars that can be parked
    car_area = 10
    num_cars = usable_area / car_area

    # Display the number of cars that can be parked
    result = num_cars
    return result

print(solution())