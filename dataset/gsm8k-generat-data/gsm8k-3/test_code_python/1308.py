def solution():
    """Jake is worried about how much time he has spent watching a new show. He spent half the day on Monday watching his show, 4 hours on Tuesday, a quarter of the day on Wednesday, and half as much time watching the show on Thursday as he had done before. On Friday, he finished the show. If the entire show is 52 hours long, how many hours did Jake watch on Friday?"""
    # Define various time ratios
    MONDAY_RATIO = 0.5
    TUESDAY_RATIO = 4 / 24
    WEDNESDAY_RATIO = 0.25
    THURSDAY_RATIO = 0.5

    # Calculate the total time watched from Monday to Thursday
    total_ratio = MONDAY_RATIO + TUESDAY_RATIO + WEDNESDAY_RATIO + THURSDAY_RATIO
    total_time = total_ratio * 52

    # Calculate the remaining time after Thursday
    remaining_time = 52 - total_time

    # Calculate the time watched on Friday
    friday_time = remaining_time

    # Display the time watched on Friday
    result = friday_time
    return result

print(solution())