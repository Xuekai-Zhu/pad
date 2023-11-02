def solution():
    # Calculate the number of striped nails
    striped_nails = 20 - 6 - 8  # number of purple and blue nails subtracted from total number of nails
    # Calculate the percentage of nails painted blue and striped
    blue_percentage = (8 / 20) * 100
    striped_percentage = (striped_nails / 20) * 100
    # Calculate the difference in percentage points
    percentage_difference = abs(blue_percentage - striped_percentage)
    result = percentage_difference
    return result

print(solution())