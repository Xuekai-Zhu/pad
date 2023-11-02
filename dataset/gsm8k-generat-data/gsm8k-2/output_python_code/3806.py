def solution():
    """As a special treat, Georgia makes muffins and brings them to her students on the first day of every month. Her muffin recipe only makes 6 muffins and she has 24 students. How many batches of muffins does Georgia make in 9 months?"""
    muffins_per_batch = 6
    students = 24
    batches_per_month = students // muffins_per_batch
    batches_per_year = batches_per_month * 12
    batches_in_9_months = batches_per_year * 0.75
    result = batches_in_9_months
    return result

print(solution())