def solution():
    """Amy is building 2 3 ft long by 3 ft wide garden beds and 2 4ft long by 3 ft wide garden beds.  What is the total sq ft of growing space that she will have?"""
    # Define the dimensions of each garden bed
    bed1_length = 3
    bed1_width = 3
    bed2_length = 4
    bed2_width = 3

    # Calculate the area of each garden bed
    bed1_area = bed1_length * bed1_width
    bed2_area = bed2_length * bed2_width

    # Calculate the total area of all the garden beds
    total_area = 2 * bed1_area + 2 * bed2_area

    # Display the total area
    result = total_area
    return result

print(solution())