def solution():
    gas_tank = 12  # Jim's gas tank can hold 12 gallons
    fuel_left = 2/3 * gas_tank  # Jim has 2/3 of a tank left
    distance_to_work = 10  # Jim's work is 10 miles away from his house
    distance_travelled = distance_to_work * 2  # Jim drives to work and back home everyday

    # Calculate the miles per gallon Jim gets
    mpg = (distance_travelled / fuel_left)
    result = mpg
    return result

print(solution())