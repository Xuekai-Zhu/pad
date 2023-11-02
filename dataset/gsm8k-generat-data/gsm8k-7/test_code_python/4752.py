def solution():
    total_nails = 20
    purple_nails = 6
    blue_nails = 8

    # Calculate the number of striped nails
    striped_nails = total_nails - purple_nails - blue_nails

    # Calculate the percentage of nails painted blue
    blue_percent = (blue_nails / total_nails) * 100

    # Calculate the percentage of nails painted striped
    striped_percent = (striped_nails / total_nails) * 100

    # Calculate the difference in percentage points between blue and striped nails
    difference = abs(blue_percent - striped_percent)

    result = difference
    return result

print(solution())