def solution():
    """As a special treat, Georgia makes muffins and brings them to her students on the first day of every month. Her muffin recipe only makes 6 muffins and she has 24 students. How many batches of muffins does Georgia make in 9 months?"""
    
    # Define the number of students and muffins per batch
    students = 24
    muffins_per_batch = 6

    # Calculate the number of batches needed per month
    batches_per_month = students / muffins_per_batch

    # Calculate the total number of batches needed for 9 months
    total_batches = batches_per_month * 9

    result = int(total_batches)
    return result

print(solution())