def solution():
    # Define the ratio of green houses to yellow houses
    green_to_yellow = 3

    # Calculate the number of yellow houses
    yellow_houses = 90 / green_to_yellow

    # Calculate the number of red houses
    red_houses = yellow_houses + 40

    # Calculate the total number of houses
    total_houses = green_houses + yellow_houses + red_houses

    # Calculate the number of non-yellow houses
    non_yellow_houses = total_houses - yellow_houses

    result = non_yellow_houses
    return result

print(solution())