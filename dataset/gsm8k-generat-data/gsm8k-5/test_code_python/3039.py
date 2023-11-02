def solution():
    running_current = 40  # The running current of each appliance is 40A
    starting_current = 2 * running_current  # The starting current required by each appliance is twice its running current
    total_current = 3 * starting_current  # The total current required by all three appliances

    # The minimum current load the transformer must be able to carry is the total starting current required by all three appliances
    result = total_current
    return result

print(solution())