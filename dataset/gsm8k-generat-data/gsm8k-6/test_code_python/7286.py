def solution():
    # Calculate Greg's remaining time to do homework
    greg_time = 18 - 6

    # Calculate Patrick's remaining time to do homework
    patrick_time = 2 * greg_time - 4

    # Calculate the total time they all have left to finish their homework
    total_time = greg_time + patrick_time + 18

    result = total_time
    return result

print(solution())