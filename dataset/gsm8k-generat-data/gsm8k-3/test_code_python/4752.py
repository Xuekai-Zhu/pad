def solution():
    """Jill is painting her 20 toenails and fingernails. She paints 6 of her nails purple, 8 of them blue, and the rest striped. What is the difference in percentage points between the percentage of nails painted blue and the percentage painted striped?"""
    # Define the total number of nails
    total_nails = 20

    # Define the number of nails painted blue
    blue_nails = 8

    # Calculate the number of nails painted striped
    striped_nails = total_nails - blue_nails - 6

    # Calculate the percentage of nails painted blue
    blue_percentage = (blue_nails / total_nails) * 100

    # Calculate the percentage of nails painted striped
    striped_percentage = (striped_nails / total_nails) * 100

    # Calculate the difference in percentage points between blue and striped nails
    difference = abs(blue_percentage - striped_percentage)

    # Display the difference
    result = difference
    return result

print(solution())