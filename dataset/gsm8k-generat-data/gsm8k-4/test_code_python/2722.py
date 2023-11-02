def solution():
    """Jim is wondering how many miles each gallon of gas gets him. His gas tank is 12 gallons. He has 2/3 of a tank left after he drives to and from work, which is 10 miles away from his house. How many miles per gallon does he get?"""
    # Define the gas tank volume and the distance to work
    gas_tank = 12
    distance_to_work = 10

    # Calculate the total distance Jim can travel with a full tank of gas
    total_distance = gas_tank * (2/3 + 1)

    # Calculate the distance Jim traveled to and from work
    work_distance = distance_to_work * 2

    # Calculate the remaining distance Jim can travel after going to and from work
    remaining_distance = total_distance - work_distance

    # Calculate the miles per gallon
    mpg = remaining_distance / (gas_tank * (1/3))

    result = mpg
    return result

print(solution())