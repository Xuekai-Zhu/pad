def solution():
    # Calculate the number of marbles left in the jar after day 1
    remaining_marbles = 30 * (2/5)  # they took 3/5 of the marbles, so 2/5 are left
    # Calculate the number of marbles Cleo took on day 3
    cleo_marbles = remaining_marbles * (1/2)
    result = cleo_marbles
    return result

print(solution())