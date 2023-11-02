def solution():
    hanuman_duties = ["strength", "knowledge", "victory"]
    athena_duties = ["war", "wisdom"]
    overlap = [duty for duty in hanuman_duties if duty in athena_duties]
    if overlap:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())