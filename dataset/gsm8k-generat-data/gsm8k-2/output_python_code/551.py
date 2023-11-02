def solution():
    """James paves a new parking lot. It is 400 feet by 500 feet. Only 80% of that is usable for parking. It takes 10 square feet to park a car. How many cars can be parked?"""
    lot_length = 400
    lot_width = 500
    usable_percent = 0.8
    usable_length = lot_length * usable_percent
    usable_width = lot_width * usable_percent
    usable_area = usable_length * usable_width
    car_area = 10
    cars_parked = usable_area / car_area
    result = int(cars_parked)
    return result

print(solution())