def solution():
 
    initial_marbles = 12
    dropped_marbles = initial_marbles / 2
    second_marble_attempt = 10
    new_marbles = 25
    total_marbles = initial_marbles + second_marble_attempt + new_marbles - dropped_marbles
    result = total_marbles
    return result

print(solution())