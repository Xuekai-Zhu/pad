def solution():
    total_marbles = 500  # Cindy had 500 marbles
    friends = 4  # Cindy gave marbles to 4 friends
    marbles_given = 80 * friends  # Cindy gave each friend 80 marbles

    # Calculate the number of marbles Cindy has remaining
    marbles_remaining = total_marbles - marbles_given

    # Calculate four times the number of marbles Cindy has remaining
    result = 4 * marbles_remaining
    return result

print(solution())