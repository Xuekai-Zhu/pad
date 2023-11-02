def solution():
    """Mike changes tires on different vehicles. He changes all the tires on 12 motorcycles and all the tires on 10 cars. How many tires did he change?"""
    motorcycle_tires = 12 * 2  # each motorcycle has 2 tires
    car_tires = 10 * 4  # each car has 4 tires
    total_tires = motorcycle_tires + car_tires
    result = total_tires
    return result

print(solution())