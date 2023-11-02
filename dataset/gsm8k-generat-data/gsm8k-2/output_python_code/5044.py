def solution():
    """Last week, Mr. Sanchez bought 6 feet of rope for their class activity. He found that he lacks rope for the activity so this week, he bought 4 feet less than last week. Since there are 12 inches in a foot, how many inches of ribbon did Mr. Sanchez buy in all?"""
    last_week_rope = 6
    this_week_rope = last_week_rope - 4
    total_rope = last_week_rope + this_week_rope
    inches_per_foot = 12
    total_inches = total_rope * inches_per_foot
    result = total_inches
    return result

print(solution())