def solution():
    original_volume = 500  # cm³
    increase_per_hour = (2/5) * original_volume
    volume_after_2_hours = original_volume + (2 * increase_per_hour)
    result = volume_after_2_hours
    return result

print(solution())