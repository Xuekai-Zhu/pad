def solution():
    vacuuming_time_per_week = 30 * 3 / 60  # Aron spends 30 minutes per day, 3 times a week, and there are 60 minutes in an hour
    dusting_time_per_week = 20 * 2 / 60  # Aron spends 20 minutes per day, 2 times a week, and there are 60 minutes in an hour
    total_cleaning_time_per_week = vacuuming_time_per_week + dusting_time_per_week

    result = total_cleaning_time_per_week
    return result

print(solution())