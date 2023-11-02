def solution():
    """Jim is wondering how many miles each gallon of gas gets him. His gas tank is 12 gallons. He has 2/3 of a tank left after he drives to and from work, which is 10 miles away from his house. How many miles per gallon does he get?"""
    # Define the size of Jim's gas tank and the distance of his daily commute
    GAS_TANK_SIZE = 12
    DAILY_COMMUTE_DISTANCE = 2 * 10

    # Calculate the amount of gas Jim has left in his tank after his daily commute
    remaining_gas = GAS_TANK_SIZE * (2/3)

    # Calculate the distance Jim can travel with the remaining gas
    remaining_distance = remaining_gas * miles_per_gallon

    # Calculate the miles per gallon Jim gets
    miles_per_gallon = remaining_distance / remaining_gas

    # Display the miles per gallon Jim gets
    result = miles_per_gallon
    return result

print(solution())