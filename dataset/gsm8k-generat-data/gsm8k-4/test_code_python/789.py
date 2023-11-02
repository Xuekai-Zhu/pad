def solution():
    """James hurt himself exercising. The pain subsided after 3 days, but he knew that the injury would take at least 5 times that long to fully heal. After that, he wanted to wait another 3 days before he started working out again. If he wants to wait 3 weeks after that to start lifting heavy again, how long until he can lift heavy again?"""
    # Define the number of days to fully heal the injury
    full_heal_time = 3 * 5

    # Define the number of days to wait after the injury has fully healed before starting to work out again
    wait_time = 3

    # Define the number of weeks to wait after starting to work out again before lifting heavy
    heavy_wait_time = 3

    # Calculate the total number of days before James can lift heavy again
    total_days = full_heal_time + wait_time + (heavy_wait_time * 7)

    result = total_days
    return result

print(solution())