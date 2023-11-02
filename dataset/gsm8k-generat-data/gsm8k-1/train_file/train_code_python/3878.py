def solution():
    """Bruce can make 15 batches of pizza dough using a sack of flour. If he uses 5 sacks of flour per day, how many pizza doughs can he make in a week?"""
    batches_per_sack = 15
    sacks_per_day = 5
    days_per_week = 7
    total_batches = batches_per_sack * sacks_per_day * days_per_week
    result = total_batches
    return result

print(solution())