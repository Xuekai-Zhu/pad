def solution():
    # Calculate the number of times Pastor Paul prays in a week
    paul_weekly_prayers = 20 * 6 + 2 * 20  # 20 times per day on weekdays, and twice as much on Sunday

    # Calculate the number of times Pastor Bruce prays in a week
    bruce_weekly_prayers = 0.5 * paul_weekly_prayers + 2 * 20  # half as much as Pastor Paul on weekdays, and twice as much on Sunday

    # Calculate the difference in the number of times they pray
    difference = paul_weekly_prayers - bruce_weekly_prayers
    result = difference
    return result

print(solution())