def solution():
    """The distance across a country is 8205 kilometers. Amelia started at one end and drove 907 kilometers on Monday and 582 kilometers on Tuesday. How many kilometers does Amelia still have to drive to make it across the country?"""
    # Define the distance across the country and Amelia's total distance driven
    total_distance = 8205
    amelia_distance = 907 + 582

    # Calculate the remaining distance to be driven
    remaining_distance = total_distance - amelia_distance

    # Return the result
    result = remaining_distance
    return result

print(solution())