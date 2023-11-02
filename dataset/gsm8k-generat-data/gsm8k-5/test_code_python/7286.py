def solution():
    # Calculate the amount of time Patrick has left to finish his homework
    greg_time = 18 - 6  # Greg has six hours less than Jacob left to finish his homework
    patrick_time = 2 * greg_time - 4  # Patrick has 4 hours less than twice the amount of time that Greg has left to finish his homework

    # Calculate the total amount of time they all have left
    total_time = jacob_time + greg_time + patrick_time
    result = total_time
    return result

print(solution())