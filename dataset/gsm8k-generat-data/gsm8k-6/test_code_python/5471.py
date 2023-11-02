def solution():
    # Calculate the number of situps Hani did
    hani_rate = 4 + 3  # Hani does 3 more situps per minute than Diana
    hani_situps = hani_rate * 40 / 4  # Hani did her situps at the same time as Diana, so we use the same time frame
    total_situps = hani_situps + 40  # Total number of situps done by both of them
    result = total_situps
    return result

print(solution())