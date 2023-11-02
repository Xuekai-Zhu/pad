def solution():
    total_spaces = 1000  # The parking lot has 1000 spaces
    section1_spaces = 320  # Section 1 has 320 spaces
    section3_spaces = (total_spaces - section1_spaces) // 4  # Section 3 has 1/4 of the remaining spaces
    section2_spaces = section3_spaces + 200  # Section 2 has 200 more spaces than Section 3

    result = section2_spaces
    return result

print(solution())