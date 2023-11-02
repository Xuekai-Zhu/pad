def solution():
    """Patrick has 4 hours less than twice the amount of time that Greg has left to finish his homework. Greg has six hours less than Jacob left to finish his homework. If Jacob has 18 hours left to finish his homework, calculate the total number of hours they all have left to finish their homework?"""
    # Calculate Greg's remaining time
    greg_time = 18 - 6

    # Calculate Patrick's remaining time
    patrick_time = (2 * greg_time) - 4

    # Calculate the total remaining time
    total_time = jacob_time + greg_time + patrick_time

    # return the result
    result = total_time
    return result

print(solution())