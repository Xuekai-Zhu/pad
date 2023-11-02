def solution():
    
    total_kids = 2000
    soccer_camp_kids = total_kids / 2
    morning_soccer_kids = soccer_camp_kids / 4
    afternoon_soccer_kids = soccer_camp_kids - morning_soccer_kids
    result = afternoon_soccer_kids
    return result

print(solution())