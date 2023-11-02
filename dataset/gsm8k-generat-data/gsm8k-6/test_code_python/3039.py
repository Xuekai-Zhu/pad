def solution():
    # Calculate the starting current for each machinery
    starting_current = 2*40  

    # Calculate the total starting current required for all three machinery
    total_starting_current = starting_current * 3  

    # The minimum current load that the transformer must be able to carry is the total starting current
    result = total_starting_current
    return result

print(solution())