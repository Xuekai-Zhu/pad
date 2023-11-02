def solution():
    
    total_campers = 150
    two_weeks_ago = 40
    three_weeks_ago = two_weeks_ago - 10
    last_week = total_campers - (two_weeks_ago + three_weeks_ago)
    result = last_week
    return result

print(solution())