def solution():
    """Janice gave all three dozens of pebbles from her trip to her friends. Each of her friends got 4 pebbles. How many friends received pebbles?"""
    # Define the number of pebbles in a dozen
    PEBBLES_PER_DOZEN = 12

    # Calculate the total number of pebbles Janice gave away
    total_pebbles = 3 * PEBBLES_PER_DOZEN

    # Calculate the number of friends who received pebbles
    num_friends = total_pebbles // 4

    # Display the number of friends who received pebbles
    result = num_friends
    return result

print(solution())