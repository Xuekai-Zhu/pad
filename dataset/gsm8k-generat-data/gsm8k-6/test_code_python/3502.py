def solution():
    # Calculate the total number of crickets Spike hunts per day
    morning_crickets = 5
    afternoon_crickets = 3 * morning_crickets  # Spike hunts three times the number of crickets he hunts in the morning
    evening_crickets = afternoon_crickets
    total_crickets = morning_crickets + afternoon_crickets + evening_crickets
    result = total_crickets
    return result

print(solution())