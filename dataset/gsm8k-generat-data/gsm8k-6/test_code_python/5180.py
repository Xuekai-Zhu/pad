def solution():
    # Calculate the number of kids going to soccer camp in the morning
    morning_soccer_camp = (1/4) * (1/2) * 2000  # 1/4 of the kids going to soccer camp, and half of the kids are going to soccer camp

    # Calculate the number of kids going to soccer camp in the afternoon
    afternoon_soccer_camp = (1/2) * 2000 - morning_soccer_camp  # half of the kids are going to soccer camp, minus those going in the morning
    result = afternoon_soccer_camp
    return result

print(solution())