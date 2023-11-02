def solution():
    
    lot_area = 400 * 500
    usable_area = lot_area * 0.8
    car_area = 10
    num_cars = usable_area / car_area
    result = num_cars
    return result

print(solution())