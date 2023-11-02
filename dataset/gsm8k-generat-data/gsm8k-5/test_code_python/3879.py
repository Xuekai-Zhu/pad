def solution():
    batches_per_sack = 15  # Bruce can make 15 batches of pizza dough using a sack of flour
    sacks_per_day = 5  # Bruce uses 5 sacks of flour per day
    days_per_week = 7  # There are 7 days in a week

    # Calculate the total number of batches of pizza dough Bruce can make in a week
    total_batches = batches_per_sack * sacks_per_day * days_per_week
    result = total_batches
    return result

print(solution())