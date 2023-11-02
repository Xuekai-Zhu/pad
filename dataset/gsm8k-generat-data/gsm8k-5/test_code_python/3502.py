def solution():
    morning_crickets = 5  # Spike hunts 5 crickets in the morning
    afternoon_crickets = 3 * morning_crickets  # Spike hunts three times as many crickets in the afternoon/evening
    total_crickets = morning_crickets + afternoon_crickets  # Add together the number of crickets from both times of day
    result = total_crickets
    return result

print(solution())