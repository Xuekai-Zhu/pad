def solution():
    Sam_marbles_start = 2 * Steve_marbles_start
    Sally_marbles_start = Sam_marbles_start - 5
    Sam_marbles_end = Sam_marbles_start - 3
    Sally_marbles_end = Sally_marbles_start + 3
    Steve_marbles_end = Sam_marbles_end - 3
    result = Steve_marbles_end
    return result

print(solution())