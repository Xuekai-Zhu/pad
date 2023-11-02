def solution():
    """Jill is painting her 20 toenails and fingernails. She paints 6 of her nails purple, 8 of them blue, and the rest striped. What is the difference in percentage points between the percentage of nails painted blue and the percentage painted striped?"""
    # Define the total number of nails
    total_nails = 20

    # Calculate the number of purple and blue nails
    purple_nails = 6
    blue_nails = 8

    # Calculate the number of striped nails
    striped_nails = total_nails - purple_nails - blue_nails

    # Calculate the percentage of nails painted blue
    blue_percentage = (blue_nails / total_nails) * 100

    # Calculate the percentage of nails painted striped
    striped_percentage = (striped_nails / total_nails) * 100

    # Calculate the difference in percentage points
    difference = abs(blue_percentage - striped_percentage)

    result = difference
    return result

print(solution())