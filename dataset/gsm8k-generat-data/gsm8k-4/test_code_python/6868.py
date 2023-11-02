def solution():
    """Tim spends 1 hour a day meditating. He spends twice as much time reading. How much time a week does he spend reading?"""
    # Define the number of hours Tim spends meditating each day
    meditate_hours_per_day = 1

    # Calculate the number of hours Tim spends reading each day
    read_hours_per_day = meditate_hours_per_day * 2

    # Calculate the number of hours Tim spends reading each week
    read_hours_per_week = read_hours_per_day * 7

    # Return the result
    result = read_hours_per_week
    return result

print(solution())