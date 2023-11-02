def solution():
    
    total_marbles = 12 + 28
    marbles_taken = (1/4) * total_marbles
    remaining_marbles = total_marbles - 2*marbles_taken
    result = remaining_marbles
    return result

print(solution())