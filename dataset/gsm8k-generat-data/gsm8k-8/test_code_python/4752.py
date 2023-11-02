def solution():
    total_nails = 20
    purple_nails = 6
    blue_nails = 8
    striped_nails = total_nails - purple_nails - blue_nails

    # Calculate the percentage of blue and striped nails
    blue_percentage = (blue_nails / total_nails) * 100
    striped_percentage = (striped_nails / total_nails) * 100

    # Calculate the difference in percentage points
    difference = round(abs(blue_percentage - striped_percentage), 2)
    result = difference
    return result

print(solution())