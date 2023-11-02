def solution():
    """The carousel at the fair has 3 blue horses, three times that many purple horses, twice as many green horses as purple horses, and 1/6th as many gold horses as green horses. How many horses are there total?"""
    # Define the number of blue horses
    blue_horses = 3

    # Calculate the number of purple horses
    purple_horses = 3 * blue_horses

    # Calculate the number of green horses
    green_horses = 2 * purple_horses

    # Calculate the number of gold horses
    gold_horses = green_horses / 6

    # Calculate the total number of horses
    total_horses = blue_horses + purple_horses + green_horses + gold_horses

    # Return the result
    result = total_horses
    return result

print(solution())