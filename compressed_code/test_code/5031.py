def solution():
    
    total_students = 500
    junior_percent = 0.4
    junior_count = total_students * junior_percent
    sports_percent = 0.7
    sports_count = junior_count * sports_percent
    result = sports_count
    return result

print(solution())