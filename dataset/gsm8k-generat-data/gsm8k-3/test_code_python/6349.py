def solution():
    """Isabella has three times as many green houses as yellow houses. She also has 40 fewer yellow houses than red houses. If she has 90 green houses, how many of her houses are not yellow?"""
    # Define the number of green houses
    green_houses = 90

    # Calculate the number of yellow houses
    yellow_houses = green_houses / 3

    # Calculate the number of red houses
    red_houses = yellow_houses + 40

    # Calculate the total number of houses
    total_houses = green_houses + yellow_houses + red_houses

    # Calculate the number of houses that are not yellow
    non_yellow_houses = total_houses - yellow_houses

    # Display the number of non-yellow houses
    result = non_yellow_houses
    return result

print(solution())