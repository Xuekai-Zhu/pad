def solution():
    rows = 7  # Chairs are arranged in 7 rows
    chairs_per_row = 12  # There are 12 chairs in each row
    extra_chairs = 11  # Some people grabbed 11 extra chairs and placed them at the back

    # Calculate the total number of chairs before the extra chairs were added
    total_chairs_before = rows * chairs_per_row

    # Calculate the total number of chairs after the extra chairs were added
    total_chairs_after = total_chairs_before + extra_chairs

    result = total_chairs_after
    return result

print(solution())