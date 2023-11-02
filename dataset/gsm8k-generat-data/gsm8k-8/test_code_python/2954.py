def solution():
    # Define known values
    total_spaces = 1000
    section1_spaces = 320

    # Calculate section 3 spaces
    section3_spaces = (total_spaces - section1_spaces) / 3

    # Calculate section 2 spaces
    section2_spaces = section3_spaces + 200

    result = section2_spaces
    return result

print(solution())