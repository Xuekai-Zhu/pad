def solution():
    """Tom bought 10 packages of miniature racing cars. Each package contains five cars. He gave each of his two nephews 1/5 of the cars. How many miniature racing cars are left with Tom?"""
    total_cars = 10 * 5
    nephew_cars = (1/5) * total_cars * 2
    remaining_cars = total_cars - nephew_cars
    result = remaining_cars
    return result

print(solution())