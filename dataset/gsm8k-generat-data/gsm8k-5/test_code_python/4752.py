def solution():
    total_nails = 20  # Jill is painting 20 nails
    purple_nails = 6  # Jill paints 6 of her nails purple
    blue_nails = 8  # Jill paints 8 of her nails blue
    striped_nails = total_nails - purple_nails - blue_nails  # Jill paints the rest of her nails striped

    # Calculate the percentage of nails painted blue
    blue_percentage = (blue_nails / total_nails) * 100

    # Calculate the percentage of nails painted striped
    striped_percentage = (striped_nails / total_nails) * 100

    # Calculate the difference in percentage points between blue and striped nails
    difference = abs(blue_percentage - striped_percentage)
    result = difference
    return result

print(solution())