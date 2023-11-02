def solution():
    """
    Farmer Steven needs to load his truck up with compost. His tractor can scoop up compost at a rate of 75 pounds per minute.
    Steven's son, Darrel, wants to help. Using a shovel, Darrel can scoop up 10 pounds per minute.
    How much time, in minutes, would it take for the two working together at the same time to load up 2550 pounds of compost into the truck?
    """
    tractor_rate = 75
    darrel_rate = 10
    total_rate = tractor_rate + darrel_rate
    compost_needed = 2550
    time_to_load = compost_needed / total_rate
    result = time_to_load
    return result

print(solution())