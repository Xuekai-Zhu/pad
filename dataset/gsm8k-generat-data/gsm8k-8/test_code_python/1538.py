def solution():
    # Define starting values
    paintings = 2
    multiplier = 1

    # Loop through 5 days and update values
    for i in range(5):
        paintings += 2 ** (multiplier)
        multiplier += 1

    result = paintings
    return result

print(solution())