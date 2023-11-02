def solution():
    
    initial_lambs = 6
    extra_babies = 2*2
    traded_lambs = 3
    extra_lambs = 7
    current_lambs = initial_lambs + extra_babies - traded_lambs + extra_lambs
    result = current_lambs
    return result

print(solution())