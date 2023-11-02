def solution():
    # Calculate the total number of cookies available
    total_cookies = (15 / 3) * 24

    # Calculate the total number of chores her siblings can do in one week
    total_chores_per_week = 4 * 2

    # Calculate the number of cookies needed for all chores in one week
    cookies_needed_per_week = total_chores_per_week * 3

    # Calculate the number of weeks Patty can go without doing chores
    weeks_without_chores = total_cookies // cookies_needed_per_week
    result = weeks_without_chores
    return result

print(solution())