def solution():
    shells_collected = 10 * 6  # Evie collects 10 shells each day for 6 days
    shells_given_away = 2  # Evie gives 2 shells away to her brother
    shells_left = shells_collected - shells_given_away  # Calculate the number of shells Evie has left
    result = shells_left
    return result

print(solution())