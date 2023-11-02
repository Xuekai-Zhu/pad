def solution():
    """Pastor Paul prays 20 times per day, except on Sunday, when he prays twice as much. Pastor Bruce prays half as much as Pastor Paul, except on Sundays, when he prays twice as much as Pastor Paul. How many more times does Pastor Paul pray than Pastor Bruce prays in a week?"""
    paul_prays_per_week = 20 * 6 + 40
    bruce_prays_per_week = (20 / 2) * 6 + (40 / 2)
    difference = paul_prays_per_week - bruce_prays_per_week
    result = difference
    return result

print(solution())