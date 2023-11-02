def solution():
    # Calculate how many times Pastor Paul prays in a week
    paul_daily_prays = 20
    paul_weekly_prays = paul_daily_prays * 6  # he doesn't pray twice on Sunday
    paul_sunday_prays = paul_daily_prays * 2
    paul_total_prays = paul_weekly_prays + paul_sunday_prays

    # Calculate how many times Pastor Bruce prays in a week
    bruce_daily_prays = paul_daily_prays / 2
    bruce_weekly_prays = bruce_daily_prays * 6  # he doesn't pray twice on Sunday
    bruce_sunday_prays = paul_sunday_prays * 2
    bruce_total_prays = bruce_weekly_prays + bruce_sunday_prays

    # Calculate the difference in their prayers
    difference = paul_total_prays - bruce_total_prays
    result = difference
    return result

print(solution())