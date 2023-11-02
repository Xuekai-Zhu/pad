def solution():
    
    last_week = 6
    this_week = last_week - 4
    total_feet = last_week + this_week
    inches_per_foot = 12
    total_inches = total_feet * inches_per_foot
    result = total_inches
    return result

print(solution())