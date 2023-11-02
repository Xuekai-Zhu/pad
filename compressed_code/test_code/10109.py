def solution():
    
    kwame_hours = 2.5
    connor_hours = 1.5
    lexia_minutes = 97
    kwame_minutes = kwame_hours * 60
    connor_minutes = connor_hours * 60
    total_minutes = kwame_minutes + connor_minutes
    diff_minutes = total_minutes - lexia_minutes
    result = diff_minutes
    return result

print(solution())