def solution():
    
    current_marbles = 30
    brother_marbles = 60
    sister_marbles = 2 * brother_marbles
    savanna_marbles = 3 * current_marbles
    total_marbles = current_marbles + brother_marbles + sister_marbles + savanna_marbles
    result = total_marbles

    return result

print(solution())