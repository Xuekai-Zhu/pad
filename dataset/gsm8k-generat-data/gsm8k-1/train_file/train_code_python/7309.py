def solution():
    """For a wedding, chairs were arranged in 7 rows with 12 chairs in each row. Some people arrived late and grabbed 11 extra chairs, placing them at the back. How many chairs were there altogether?"""
    chairs_per_row = 12
    rows = 7
    extra_chairs = 11
    total_chairs = (chairs_per_row * rows) + extra_chairs
    result = total_chairs
    return result

print(solution())