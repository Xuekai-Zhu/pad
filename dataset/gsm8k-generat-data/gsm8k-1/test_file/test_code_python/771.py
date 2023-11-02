def solution():
    """Henry needs to assemble some toys, specifically 57 cars and 73 motorcycles. Henry knows that to assemble all the toys he will need 4 wheels for each car and 2 wheels for each motorcycle. How many wheels will be left if he has a box with 650 wheels in it?"""
    cars = 57
    motorcycles = 73
    wheels_per_car = 4
    wheels_per_motorcycle = 2
    total_wheels_needed = (cars * wheels_per_car) + (motorcycles * wheels_per_motorcycle)
    wheels_left = 650 - total_wheels_needed
    result = wheels_left
    return result

print(solution())