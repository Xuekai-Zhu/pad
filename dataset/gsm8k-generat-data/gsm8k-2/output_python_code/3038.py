def solution():
    """The owner of a company needs to install a transformer to power his electrical equipment. He operates three units of machinery that require a running current of 40A each. These appliances require at least twice their running current for starting, and the transformer chosen must account for this. What is the minimum current load that his transformer of choice must be able to carry?"""
    running_current = 40
    starting_current = running_current * 2
    total_current = running_current + starting_current
    transformer_load = total_current * 3
    result = transformer_load
    return result

print(solution())