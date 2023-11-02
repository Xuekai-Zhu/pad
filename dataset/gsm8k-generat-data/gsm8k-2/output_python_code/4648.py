def solution():
    """A machine fills 150 cans of paint every 8 minutes. How many minutes does it take this machine to fill 675 cans?"""
    cans_filled_per_minute = 150 / 8
    total_cans_to_fill = 675
    time_to_fill = total_cans_to_fill / cans_filled_per_minute
    result = time_to_fill
    return result

print(solution())