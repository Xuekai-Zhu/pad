def solution():
    """Hani said she would do 3 more situps per minute than Diana would. Diana then did 40 situps at a rate of 4 situps per minute. Calculate the total number of situps they did together."""
    diana_rate = 4
    diana_situps = 40
    hani_rate = diana_rate + 3
    hani_situps = hani_rate * (diana_situps / diana_rate)
    total_situps = diana_situps + hani_situps
    result = total_situps
    return result

print(solution())