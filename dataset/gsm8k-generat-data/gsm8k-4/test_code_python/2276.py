def solution():
    """Billy is reducing raspberry juice down to make syrup. He reduces 6 quarts of juice to 1/12 of its original volume, then adds 1 cup of sugar. What is the final volume of the syrup in cups? (There are 4 cups in a quart)"""
    # Define the initial volume of raspberry juice in quarts
    initial_volume = 6

    # Calculate the reduced volume of raspberry juice in quarts
    reduced_volume = initial_volume / 12

    # Convert the reduced volume to cups
    reduced_volume_cups = reduced_volume * 4

    # Add the volume of sugar in cups
    final_volume_cups = reduced_volume_cups + 1

    # return the result
    result = final_volume_cups
    return result

print(solution())