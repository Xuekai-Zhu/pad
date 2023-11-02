def solution():
    """Carol fills up her gas tank as she is driving home for college, which is 220 miles away. She can get 20 miles to the gallon in her car, which has a 16-gallon gas tank. How many more miles will she be able to drive after she gets home and without filling her tank again?"""
    # Define the distance to Carol's college
    college_distance = 220

    # Define the miles per gallon of Carol's car
    mpg = 20

    # Define the size of Carol's gas tank
    gas_tank_size = 16

    # Calculate the number of gallons of gas Carol used to get home
    gallons_used = college_distance / mpg

    # Calculate the number of gallons of gas left in Carol's tank
    gallons_left = gas_tank_size - gallons_used

    # Calculate the number of miles Carol can still drive without filling up
    miles_left = gallons_left * mpg

    # return the result
    result = miles_left
    return result

print(solution())