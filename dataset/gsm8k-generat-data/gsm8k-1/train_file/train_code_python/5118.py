def solution():
    """If we assume all thirty 4-wheel drive cars in the parking lot have their spare tire with them, how many tires are in the parking lot?"""
    cars_with_spare_tires = 30
    tires_per_car = 4
    total_tires = cars_with_spare_tires * tires_per_car
    result = total_tires
    return result

print(solution())