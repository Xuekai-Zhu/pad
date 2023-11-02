def solution():
    total_pebbles = 3 * 12  # Janice gave three dozens of pebbles to her friends
    pebbles_per_friend = 4  # Each friend received 4 pebbles

    # Calculate the number of friends who received pebbles
    num_friends = total_pebbles // pebbles_per_friend
    result = num_friends
    return result

print(solution())