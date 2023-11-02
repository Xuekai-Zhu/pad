def solution():
    recommended_time = 5 * 60  # The recommended cooking time is 5 minutes, or 300 seconds
    time_in_oven = 45  # Bill put his fries in the oven for 45 seconds

    # Calculate how many seconds are remaining until the fries are fully cooked
    remaining_time = recommended_time - time_in_oven
    result = remaining_time
    return result

print(solution())