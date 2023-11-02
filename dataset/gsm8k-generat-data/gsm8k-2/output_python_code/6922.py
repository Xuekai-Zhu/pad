def solution():
    """Amy is building 2 3 ft long by 3 ft wide garden beds and 2 4ft long by 3 ft wide garden beds. What is the total sq ft of growing space that she will have?"""
    bed1_length = 3
    bed1_width = 3
    bed2_length = 4
    bed2_width = 3
    total_sq_ft = (bed1_length * bed1_width * 2) + (bed2_length * bed2_width * 2)
    result = total_sq_ft
    return result

print(solution())