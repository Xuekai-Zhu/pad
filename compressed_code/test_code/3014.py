def solution():
    
    batches_per_sack = 15
    sacks_per_day = 5
    days_per_week = 7
    total_sacks = sacks_per_day * days_per_week
    total_batches = total_sacks * batches_per_sack
    result = total_batches
    return result

print(solution())