def solution():
    """Patrick has 4 hours less than twice the amount of time that Greg has left to finish his homework. Greg has six hours less than Jacob left to finish his homework. If Jacob has 18 hours left to finish his homework, calculate the total number of hours they all have left to finish their homework?"""
    # Calculate the number of hours Greg has left to finish his homework
    greg_hours = 18 - 6

    # Calculate the number of hours Patrick has left to finish his homework
    patrick_hours = (2 * greg_hours) - 4

    # Calculate the total number of hours they all have left to finish their homework
    total_hours = jacob_hours + greg_hours + patrick_hours

    # Display the total number of hours
    result = total_hours
    return result

print(solution())