def solution():
    green_to_yellow_ratio = 3  # Isabella has three times as many green houses as yellow houses
    green_houses = 90  # Isabella has 90 green houses

    # Calculate the number of yellow houses Isabella has
    yellow_houses = green_houses / green_to_yellow_ratio

    # Calculate the number of red houses Isabella has
    red_houses = yellow_houses + 40

    # Calculate the total number of houses Isabella has
    total_houses = green_houses + yellow_houses + red_houses

    # Calculate the number of houses that are not yellow
    not_yellow_houses = total_houses - yellow_houses
    result = not_yellow_houses
    return result

print(solution())