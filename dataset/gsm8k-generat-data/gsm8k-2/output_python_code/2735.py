def solution():
    """Paul lives in a 5th story apartment. He makes 3 trips out from and back to his apartment throughout the day each day of a week. How many feet does he travel vertically in total over the week if each story is 10 feet tall?"""
    stories = 5
    trips_per_day = 3
    days_per_week = 7
    feet_per_story = 10
    total_feet = 2 * (stories * feet_per_story) * trips_per_day * days_per_week
    result = total_feet
    return result

print(solution())