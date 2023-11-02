def solution():
    cans_first_week = 158  # Kaiden collected 158 cans during his first week
    cans_second_week = 259  # Kaiden collected 259 cans during his second week
    goal = 500  # Kaiden's goal is to collect 500 cans

    # Calculate how many more cans Kaiden needs to collect to reach his goal
    remaining_cans = goal - (cans_first_week + cans_second_week)
    result = remaining_cans
    return result

print(solution())