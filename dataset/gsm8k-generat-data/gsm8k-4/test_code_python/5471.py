def solution():
    """Hani said she would do 3 more situps per minute than Diana would. Diana then did 40 situps at a rate of 4 situps per minute. Calculate the total number of situps they did together."""
    # Calculate the number of situps Diana did in total
    diana_situps = 40

    # Calculate the rate at which Diana did situps
    diana_rate = 4

    # Calculate the number of situps Hani said she would do per minute
    hani_rate = diana_rate + 3

    # Calculate the total number of minutes
    total_minutes = diana_situps / diana_rate

    # Calculate the total number of situps Hani did
    hani_situps = hani_rate * total_minutes

    # Calculate the total number of situps they did together
    total_situps = diana_situps + hani_situps

    result = total_situps
    return result

print(solution())