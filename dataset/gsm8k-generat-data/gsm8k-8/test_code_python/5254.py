def solution():
    # Define the initial number of plain pebbles
    plain_pebbles = 40

    # Define the number of red and blue pebbles
    red_pebbles = 9
    blue_pebbles = 13

    # Calculate the remaining number of plain pebbles after painting red and blue ones
    remaining_pebbles = plain_pebbles - red_pebbles - blue_pebbles

    # Divide the remaining pebbles into 3 groups and paint them purple, yellow, and green.
    purple_pebbles = remaining_pebbles // 3
    yellow_pebbles = remaining_pebbles // 3
    green_pebbles = remaining_pebbles // 3

    # Calculate the difference between blue and yellow pebbles
    difference = blue_pebbles - yellow_pebbles

    result = difference
    return result

print(solution())