def solution():
    """Billy is reducing raspberry juice down to make syrup. He reduces 6 quarts of juice to 1/12 of its original volume, then adds 1 cup of sugar. What is the final volume of the syrup in cups? (There are 4 cups in a quart)"""
    # Define the initial volume of raspberry juice in quarts
    juice_vol = 6

    # Calculate the final volume of raspberry syrup in quarts
    syrup_vol = juice_vol / 12

    # Convert the final volume of raspberry syrup to cups
    syrup_cups = syrup_vol * 4

    # Add 1 cup of sugar to the final volume of raspberry syrup
    total_cups = syrup_cups + 1

    # Display the final volume of raspberry syrup in cups
    result = total_cups
    return result

print(solution())