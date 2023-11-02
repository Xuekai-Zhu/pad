def solution():
    muffins_per_batch = 6  # Georgia's recipe makes 6 muffins per batch
    students = 24  # Georgia has 24 students
    batches_per_month = (students // muffins_per_batch) + (1 if students % muffins_per_batch != 0 else 0)  # Number of batches Georgia needs to make each month
    months = 9  # Georgia wants to make muffins for 9 months

    # Calculate the total number of batches Georgia needs to make
    total_batches = batches_per_month * months
    result = total_batches
    return result

print(solution())