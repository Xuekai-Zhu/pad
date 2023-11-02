def solution():
    rows = 7
    chairs_per_row = 12
    extra_chairs = 11

    # Calculate the total number of chairs in the original arrangement
    total_chairs = rows * chairs_per_row

    # Add the extra chairs to the total number of chairs
    total_chairs += extra_chairs

    result = total_chairs
    return result

print(solution())