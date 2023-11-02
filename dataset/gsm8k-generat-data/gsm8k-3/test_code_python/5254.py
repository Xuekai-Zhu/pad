def solution():
    """Shawn collected 40 plain pebbles. He painted 9 pebbles red and 13 pebbles blue. He then divided the remaining pebbles equally into 3 groups, and painted them purple, yellow, and green. What is the difference between the number of blue and yellow pebbles?"""
    # Define the total number of pebbles collected
    total_pebbles = 40

    # Define the number of red and blue pebbles
    red_pebbles = 9
    blue_pebbles = 13

    # Calculate the number of remaining pebbles
    remaining_pebbles = total_pebbles - red_pebbles - blue_pebbles

    # Divide the remaining pebbles equally into 3 groups and paint them purple, yellow, and green
    purple_pebbles = remaining_pebbles // 3
    yellow_pebbles = remaining_pebbles // 3
    green_pebbles = remaining_pebbles // 3

    # Calculate the difference between the number of blue and yellow pebbles
    difference = blue_pebbles - yellow_pebbles

    # Display the difference
    result = difference
    return result

print(solution())