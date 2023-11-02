def solution():
    reese_height = 60
    daisy_height = reese_height + 8
    parker_height = daisy_height - 4

    # Calculate the total height of the three of them
    total_height = reese_height + daisy_height + parker_height

    # Calculate the average height
    average_height = total_height / 3
    result = average_height
    return result

print(solution())