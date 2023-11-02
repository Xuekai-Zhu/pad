def solution():
    total_kids = 2000

    # Calculate the number of kids going to soccer camp
    soccer_camp_kids = total_kids / 2

    # Calculate the number of kids going to soccer camp in the morning
    morning_soccer_kids = soccer_camp_kids / 4

    # Calculate the number of kids going to soccer camp in the afternoon
    afternoon_soccer_kids = soccer_camp_kids - morning_soccer_kids
    result = afternoon_soccer_kids
    return result

print(solution())