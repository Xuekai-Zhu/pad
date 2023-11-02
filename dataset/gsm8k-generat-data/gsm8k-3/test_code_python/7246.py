def solution():
    """Pastor Paul prays 20 times per day, except on Sunday, when he prays twice as much.  Pastor Bruce prays half as much as Pastor Paul, except on Sundays, when he prays twice as much as Pastor Paul.  How many more times does Pastor Paul pray than Pastor Bruce prays in a week?"""
    # Calculate the number of times Pastor Paul prays in a week
    paul_weekly_count = 20 * 6 + 2 * 20

    # Calculate the number of times Pastor Bruce prays in a week
    bruce_weekly_count = 0.5 * paul_weekly_count + 2 * 20

    # Calculate the difference in the number of times they pray
    difference = paul_weekly_count - bruce_weekly_count

    # Display the difference
    result = difference
    return result

print(solution())