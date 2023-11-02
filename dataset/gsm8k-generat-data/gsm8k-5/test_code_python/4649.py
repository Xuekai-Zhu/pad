def solution():
    cans_per_minute = 150 / 8  # The machine fills 150 cans in 8 minutes, so it fills 150/8 cans per minute
    cans_to_fill = 675  # The machine needs to fill 675 cans

    # Calculate the number of minutes it takes to fill the cans
    time_to_fill = cans_to_fill / cans_per_minute
    result = time_to_fill
    return result

print(solution())