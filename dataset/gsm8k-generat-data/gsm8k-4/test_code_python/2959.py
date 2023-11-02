def solution():
    """Janice gave all three dozens of pebbles from her trip to her friends. Each of her friends got 4 pebbles. How many friends received pebbles?"""
    # Define the total number of pebbles
    total_pebbles = 3 * 12

    # Calculate the number of friends who received pebbles
    num_friends = total_pebbles // 4

    # return the result
    result = num_friends
    return result

print(solution())