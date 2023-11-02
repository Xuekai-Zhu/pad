def solution():
    # Calculate the total number of fouls John gets in 80% of the 20 games
    fouls = 5 * 0.8 * 20

    # Calculate the total number of free throws John gets
    free_throws = fouls * 2 * 0.7

    result = free_throws
    return result

print(solution())