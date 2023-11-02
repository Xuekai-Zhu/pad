def solution():
    """Diana is twice as old as Grace is today. If Grace turned 3 a year ago, how old is Diana today?"""
    grace_age = 4  # Grace turned 3 a year ago, so she is 4 now
    diana_age = grace_age * 2
    current_age = diana_age + 1  # Add one for the year that passed since Grace's last birthday
    result = current_age
    return result

print(solution())