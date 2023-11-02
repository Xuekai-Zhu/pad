def solution():
    """The owner of a company needs to install a transformer to power his electrical equipment. He operates three units of machinery that require a running current of 40A each. These appliances require at least twice their running current for starting, and the transformer chosen must account for this. What is the minimum current load that his transformer of choice must be able to carry?"""
    # Define the running current and starting current multiplier
    running_current = 40
    starting_multiplier = 2

    # Calculate the starting current for each unit of machinery
    starting_current = running_current * starting_multiplier

    # Calculate the total current load for all three units of machinery
    total_current_load = starting_current * 3

    # Display the minimum current load the transformer must be able to carry
    result = total_current_load
    return result

print(solution())