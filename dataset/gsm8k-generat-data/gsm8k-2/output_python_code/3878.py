def solution():
    """Bruce can make 15 batches of pizza dough using a sack of flour. If he uses 5 sacks of flour per day, how many pizza doughs can he make in a week?"""
    batches_per_sack = 15
    sacks_per_day = 5
    days_per_week = 7
    total_sacks = sacks_per_day * days_per_week
    total_batches = total_sacks * batches_per_sack
    result = total_batches
    return result

print(solution())