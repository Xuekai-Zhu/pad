def solution():
    """Tom bought 10 packages of miniature racing cars. Each package contains five cars. He gave each of his two nephews 1/5 of the cars. How many miniature racing cars are left with Tom?"""
    total_cars = 10 * 5
    cars_given = total_cars * (1/5) * 2
    cars_left = total_cars - cars_given
    result = cars_left
    return result

print(solution())