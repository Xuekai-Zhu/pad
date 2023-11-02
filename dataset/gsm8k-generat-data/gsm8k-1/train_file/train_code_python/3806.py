def solution():
    """As a special treat, Georgia makes muffins and brings them to her students on the first day of every month. Her muffin recipe only makes 6 muffins and she has 24 students. How many batches of muffins does Georgia make in 9 months?"""
    muffins_per_recipe = 6
    students = 24
    muffins_needed = students * 1  # Georgia needs to make a muffin for each student
    batches_needed = muffins_needed // muffins_per_recipe
    months = 9
    batches_made = batches_needed * months
    result = batches_made
    return result

print(solution())