def solution():
    """Shawn collected 40 plain pebbles. He painted 9 pebbles red and 13 pebbles blue. He then divided the remaining pebbles equally into 3 groups, and painted them purple, yellow, and green. What is the difference between the number of blue and yellow pebbles?"""
    # Define the total number of pebbles
    total_pebbles = 40

    # Paint the red and blue pebbles
    red_pebbles = 9
    blue_pebbles = 13

    # Calculate the remaining pebbles
    remaining_pebbles = total_pebbles - red_pebbles - blue_pebbles

    # Divide the remaining pebbles equally into 3 groups
    group_size = remaining_pebbles // 3

    # Paint the groups purple, yellow, and green
    purple_pebbles = group_size
    yellow_pebbles = group_size
    green_pebbles = group_size

    # Calculate the difference between the number of blue and yellow pebbles
    difference = blue_pebbles - yellow_pebbles

    # return the result
    result = difference
    return result

print(solution())