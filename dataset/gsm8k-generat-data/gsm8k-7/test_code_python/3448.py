def solution():
    num_towels = 18
    num_towels_per_use = 2
    num_days_missed = 7

    # Calculate the total number of towel uses missed during the missed week
    num_uses_missed = num_towels_per_use * num_days_missed

    # Calculate the total number of towel uses needed for the following week
    num_uses_needed = num_towels_per_use * 7

    # Calculate the total number of towel uses available
    num_uses_available = (num_towels - num_uses_missed) * 2

    # Calculate the number of days that Barney will not have clean towels
    num_days_without_clean_towels = num_uses_needed - num_uses_available
    result = num_days_without_clean_towels
    return result

print(solution())