def solution():
    meditation_time = 1  # Tim spends 1 hour a day meditating
    reading_time = meditation_time * 2  # Tim spends twice as much time reading as meditating
    days_per_week = 7  # There are 7 days in a week

    # Calculate the total time Tim spends reading in a week
    total_reading_time = reading_time * days_per_week
    result = total_reading_time
    return result

print(solution())