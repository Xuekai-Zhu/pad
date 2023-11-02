def solution():
    # Set up initial variables
    starting_marbles = 24
    marbles_lost = 4
    marbles_given_away = marbles_lost * 2
    marbles_eaten = marbles_lost / 2

    # Calculate total marbles remaining
    marbles_remaining = starting_marbles - marbles_lost - marbles_given_away - marbles_eaten
    result = marbles_remaining
    return result

print(solution())