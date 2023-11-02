def solution():
    
    total_spectators = 10000
    men = 7000
    remaining_spectators = total_spectators - men
    women = remaining_spectators / 6
    children = 5 * women
    result = children
    return result

print(solution())