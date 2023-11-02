def solution():
    """James paves a new parking lot. It is 400 feet by 500 feet. Only 80% of that is useable for parking. It takes 10 square feet to park a car. How many cars can be parked?"""
    lot_area = 400 * 500
    usable_area = lot_area * 0.8
    car_area = 10
    num_cars = usable_area / car_area
    result = num_cars
    return result

print(solution())