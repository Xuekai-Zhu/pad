def solution():
    """There are 2,000 kids in camp. If half of the kids are going to soccer camp, and 1/4 of the kids going to soccer camp are going to soccer camp in the morning, how many kids are going to soccer camp in the afternoon?"""
    total_kids = 2000
    soccer_kids = total_kids / 2
    morning_soccer_kids = soccer_kids / 4
    afternoon_soccer_kids = soccer_kids - morning_soccer_kids
    result = afternoon_soccer_kids
    return result

print(solution())