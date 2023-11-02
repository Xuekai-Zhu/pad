def solution():
    """Evelyn’s family watched 10 hours of television last week. The week before, they watched 8 hours of television. If they watch 12 hours of television next week, what is the average number of hours of television that they watch per week?"""
    last_week = 10
    previous_week = 8
    next_week = 12
    total_hours = last_week + previous_week + next_week
    average_hours = total_hours / 3
    result = average_hours
    return result

print(solution())