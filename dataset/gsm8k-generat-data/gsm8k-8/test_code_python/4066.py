def solution():
    # Calculate the number of marbles taken out of the jar on Tuesday
    tuesday_marbles = (3/5) * 30

    # Calculate the number of marbles left in the jar on Tuesday
    tuesday_leftover = 30 - tuesday_marbles

    # Calculate the number of marbles Cleo took on Wednesday
    cleo_marbles = (1/2) * tuesday_leftover

    # Calculate Cleo's total number of marbles on Wednesday
    cleo_total = cleo_marbles + 30/2

    result = cleo_total
    return result

print(solution())