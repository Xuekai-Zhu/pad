def solution():
    # Calculate the total number of push-ups to reach floor push-ups
    total_pushups = 15 + 25 + 35 + 50  # 15 reps of wall push-ups, 25 reps of high elevation push-ups, 35 reps of low elevation push-ups, and 50 reps of floor push-ups
    reps_per_week = 5 * 7  # John trains 5 days a week
    weeks = total_pushups // reps_per_week  # Round down to nearest week
    result = weeks
    return result

print(solution())