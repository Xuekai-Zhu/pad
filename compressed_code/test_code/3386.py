def solution():
    
    starting_marbles = 500
    friends = 4
    marbles_given = friends * 80
    remaining_marbles = starting_marbles - marbles_given
    result = 4 * remaining_marbles
    return result

print(solution())