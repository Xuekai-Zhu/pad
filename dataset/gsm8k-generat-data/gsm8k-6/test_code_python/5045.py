def solution():
    last_week_rope = 6  # feet of rope bought last week
    this_week_rope = last_week_rope - 4  # feet of rope bought this week
    total_rope = last_week_rope + this_week_rope  # total feet of rope bought
    total_inches = total_rope * 12  # convert feet to inches
    result = total_inches
    return result

print(solution())