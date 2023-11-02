def solution():
    total_bottles = 254
    football_bottles = 11 * 6
    soccer_bottles = 53
    lacrosse_bottles = football_bottles + 12
    rugby_bottles = total_bottles - (football_bottles + soccer_bottles + lacrosse_bottles)
    result = rugby_bottles
    
    return result

print(solution())