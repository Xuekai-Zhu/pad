def solution():
    
    
    initial_marbles = 24
    marbles_lost = 4
    marbles_given_away = 2 * marbles_lost
    marbles_eaten_by_dog = marbles_lost / 2
    
    remaining_marbles = initial_marbles - marbles_lost - marbles_given_away - marbles_eaten_by_dog
    
    result = remaining_marbles
    return result

print(solution())