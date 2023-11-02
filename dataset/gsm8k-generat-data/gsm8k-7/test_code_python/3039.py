def solution():
    running_current = 40
    starting_current = running_current * 2
    num_machines = 3

    # Calculate the total current load for all machines for starting
    total_starting_current = starting_current * num_machines

    # Calculate the minimum current load that the transformer must be able to carry
    minimum_current_load = total_starting_current
    result = minimum_current_load
    return result

print(solution())