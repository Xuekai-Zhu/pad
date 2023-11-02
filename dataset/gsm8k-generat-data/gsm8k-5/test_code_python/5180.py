def solution():
    total_kids = 2000  # There are 2,000 kids in camp
    soccer_kids = total_kids / 2  # Half of the kids are going to soccer camp
    morning_soccer_kids = soccer_kids / 4  # 1/4 of the soccer kids are going to soccer camp in the morning
    afternoon_soccer_kids = soccer_kids - morning_soccer_kids  # The remaining soccer kids are going in the afternoon

    result = afternoon_soccer_kids
    return result

print(solution())