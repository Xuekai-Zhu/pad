def solution():
    """The distance across a country is 8205 kilometers. Amelia started at one end and drove 907 kilometers on Monday and 582 kilometers on Tuesday. How many kilometers does Amelia still have to drive to make it across the country?"""
    # Define the total distance across the country
    total_distance = 8205

    # Calculate the distance Amelia has already driven
    distance_driven = 907 + 582

    # Calculate the remaining distance Amelia has to drive
    remaining_distance = total_distance - distance_driven

    # Display the remaining distance Amelia has to drive
    result = remaining_distance
    return result

print(solution())