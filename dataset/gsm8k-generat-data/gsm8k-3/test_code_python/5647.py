def solution():
    """Carol fills up her gas tank as she is driving home for college, which is 220 miles away. She can get 20 miles to the gallon in her car, which has a 16-gallon gas tank. How many more miles will she be able to drive after she gets home and without filling her tank again?"""
    # Define the distance to college
    distance_to_college = 220

    # Define the car's gas mileage and tank capacity
    GAS_MILEAGE = 20
    TANK_CAPACITY = 16

    # Calculate the number of gallons needed to travel to college
    gallons_needed = distance_to_college / GAS_MILEAGE

    # Calculate the amount of gas left in the tank after traveling to college
    gas_left = TANK_CAPACITY - gallons_needed

    # Calculate the additional distance car can travel with the remaining gas
    additional_distance = gas_left * GAS_MILEAGE

    # Display the additional distance
    result = additional_distance
    return result

print(solution())