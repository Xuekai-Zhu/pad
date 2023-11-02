def solution():
    # Calculate the starting current for each machine
    starting_current = 2 * 40

    # Calculate the total starting current required for all three machines
    total_starting_current = 3 * starting_current

    # Calculate the total minimum current load the transformer must be able to carry
    minimum_current_load = total_starting_current

    result = minimum_current_load
    return result

print(solution())