def solution():
    batches_per_sack = 15
    sacks_per_day = 5
    days_per_week = 7

    # Calculate the total number of batches of pizza dough Bruce can make in a day
    total_batches_per_day = batches_per_sack * sacks_per_day

    # Calculate the total number of batches of pizza dough Bruce can make in a week
    total_batches_per_week = total_batches_per_day * days_per_week
    result = total_batches_per_week
    return result

print(solution())