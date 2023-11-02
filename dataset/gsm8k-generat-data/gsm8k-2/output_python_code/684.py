def solution():
    """There are some kids in camp. Half of the kids are going to soccer camp, and 1/4 of the kids going to soccer camp are going to soccer camp in the morning. 750 kids are going to soccer camp in the afternoon. How many kids there in camp altogether?"""
    afternoon_kids = 750
    morning_kids = afternoon_kids / 4
    soccer_kids = afternoon_kids * 2
    total_kids = soccer_kids + morning_kids
    result = total_kids
    return result

print(solution())