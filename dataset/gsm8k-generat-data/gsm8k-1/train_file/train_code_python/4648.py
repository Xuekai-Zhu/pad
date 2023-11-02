def solution():
    """A machine fills 150 cans of paint every 8 minutes. How many minutes does it take this machine to fill 675 cans?"""
    cans_per_minute = 150 / 8
    cans_to_fill = 675
    minutes_to_fill = cans_to_fill / cans_per_minute
    result = minutes_to_fill
    return result

print(solution())