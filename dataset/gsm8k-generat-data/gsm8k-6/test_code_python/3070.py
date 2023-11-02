def solution():
    # Calculate the number of marbles Brianna has left
    marbles_lost = 4
    marbles_given_away = 2 * marbles_lost
    marbles_eaten_by_dog = marbles_lost / 2
    marbles_remaining = 24 - marbles_lost - marbles_given_away - marbles_eaten_by_dog
    result = marbles_remaining
    return result

print(solution())