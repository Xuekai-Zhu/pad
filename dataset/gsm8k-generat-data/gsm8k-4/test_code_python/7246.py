def solution():
    """Pastor Paul prays 20 times per day, except on Sunday, when he prays twice as much. Pastor Bruce prays half as much as Pastor Paul, except on Sundays, when he prays twice as much as Pastor Paul. How many more times does Pastor Paul pray than Pastor Bruce prays in a week?"""
    # Define the number of prayers per day for Pastor Paul
    paul_daily_prayers = 20

    # Calculate the number of prayers on Sunday for Pastor Paul
    paul_sunday_prayers = paul_daily_prayers * 2

    # Calculate the total number of prayers for Pastor Paul in a week
    paul_weekly_prayers = paul_daily_prayers * 6 + paul_sunday_prayers

    # Calculate the number of prayers per day for Pastor Bruce
    bruce_daily_prayers = paul_daily_prayers / 2

    # Calculate the number of prayers on Sunday for Pastor Bruce
    bruce_sunday_prayers = paul_sunday_prayers * 2

    # Calculate the total number of prayers for Pastor Bruce in a week
    bruce_weekly_prayers = bruce_daily_prayers * 6 + bruce_sunday_prayers

    # Calculate the difference between the two pastors' total weekly prayers
    difference = paul_weekly_prayers - bruce_weekly_prayers

    result = difference
    return result

print(solution())