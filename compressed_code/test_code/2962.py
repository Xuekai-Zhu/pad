def solution():
    
    muffins_per_batch = 6
    students = 24
    batches_per_month = students // muffins_per_batch
    batches_per_year = batches_per_month * 12
    batches_in_9_months = batches_per_year * 0.75
    result = batches_in_9_months
    return result

print(solution())