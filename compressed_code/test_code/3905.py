def solution():
    
    last_week_rope = 6
    this_week_rope = last_week_rope - 4
    total_rope = last_week_rope + this_week_rope
    inches_per_foot = 12
    total_inches = total_rope * inches_per_foot
    result = total_inches
    return result

print(solution())