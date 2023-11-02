def solution():
    """John has 2 umbrellas in his house and 1 in the car.  If they cost $8 each, how much did he pay in total?"""
    # Define the cost of each umbrella
    UMBRELLA_PRICE = 8

    # Define the number of umbrellas John has
    house_umbrellas = 2
    car_umbrellas = 1

    # Calculate the total cost of the umbrellas
    total_cost = (house_umbrellas + car_umbrellas) * UMBRELLA_PRICE

    # Display the total cost
    result = total_cost
    return result

print(solution())