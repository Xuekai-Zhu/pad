def solution():
    """If we assume all thirty 4-wheel drive cars in the parking lot have their spare tire with them, how many tires are in the parking lot?"""
    # Define the number of cars and wheels per car
    cars = 30
    wheels_per_car = 4

    # Calculate the total number of wheels (including spare tires)
    total_wheels = cars * (wheels_per_car + 1)

    # return the result
    result = total_wheels
    return result

print(solution())