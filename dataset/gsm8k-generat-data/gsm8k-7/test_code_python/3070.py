def solution():
    starting_marbles = 24
    marbles_lost = 4
    marbles_given_away = 2 * marbles_lost
    marbles_eaten_by_dog = marbles_lost / 2

    # Calculate the total number of marbles remaining
    total_remaining = starting_marbles - marbles_lost - marbles_given_away - marbles_eaten_by_dog
    result = total_remaining
    return result

print(solution())