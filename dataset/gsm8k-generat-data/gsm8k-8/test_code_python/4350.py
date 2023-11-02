def solution():
    # Define the total number of marbles Cindy had
    total_marbles = 500

    # Calculate the total number of marbles given to friends
    friend_marbles = 80 * 4

    # Calculate the number of marbles Cindy has remaining
    remaining_marbles = total_marbles - friend_marbles

    # Calculate four times the number of remaining marbles
    four_times_remaining = 4 * remaining_marbles

    result = four_times_remaining
    return result

print(solution())