def solution():
    half_hr_episodes = 24
    one_hr_episodes = 12

    # Calculate the total hours of the short show
    short_show_hours = half_hr_episodes * 0.5

    # Calculate the total hours of the long show
    long_show_hours = one_hr_episodes * 1

    # Calculate the total hours of TV watched
    total_hours = short_show_hours + long_show_hours
    result = total_hours
    return result

print(solution())