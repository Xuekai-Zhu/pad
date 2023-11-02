def solution():
    highest_position = "CEO"
    toilet_cleaners = ["janitors", "facility workers"]
    if highest_position not in toilet_cleaners:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())