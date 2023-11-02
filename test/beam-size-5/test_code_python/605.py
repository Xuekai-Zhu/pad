def solution():
    
    croissants_per_dozen = 12
    butter_per_dozen = 0.25
    dozens_per_day = 4
    days_per_week = 7
    total_croissants = dozens_per_day * days_per_week
    total_butter = total_croissants * butter_per_dozen
    result = total_butter
    return result

print(solution())