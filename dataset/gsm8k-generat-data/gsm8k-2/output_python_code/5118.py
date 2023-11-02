def solution():
    """If we assume all thirty 4-wheel drive cars in the parking lot have their spare tire with them, how many tires are in the parking lot?"""
    number_of_cars = 30
    tires_per_car = 4  # 4 regular tires + 1 spare tire
    total_tires = number_of_cars * tires_per_car
    result = total_tires
    return result

print(solution())