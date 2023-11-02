def solution():
    original_volume = 500
    increase_percentage = 2 / 5  # expressed as a decimal

    # First hour's increase
    first_hour_increase = original_volume * increase_percentage
    first_hour_new_volume = original_volume + first_hour_increase

    # Second hour's increase
    second_hour_increase = first_hour_new_volume * increase_percentage
    second_hour_new_volume = first_hour_new_volume + second_hour_increase

    result = second_hour_new_volume
    return result

print(solution())