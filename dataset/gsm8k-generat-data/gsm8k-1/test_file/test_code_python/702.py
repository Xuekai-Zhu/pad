def solution():
    """The local firefighters are doing a “fill the boot” fundraiser. Their goal is to raise $6300. After the first 3 hours, they have raised $2100. For how many hours do they have to fundraise in total to reach their goal, assuming an equal amount raised in every hour?"""
    goal = 6300
    raised = 2100
    remaining = goal - raised
    hours_needed = remaining / (goal / 3)
    total_hours = round(hours_needed + 3)
    result = total_hours
    return result

print(solution())