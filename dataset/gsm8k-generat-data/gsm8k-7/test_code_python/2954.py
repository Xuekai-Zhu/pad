def solution():
    total_spaces = 1000
    section1_spaces = 320

    # Let x be the number of spaces in section 3
    # Then the number of spaces in section 2 is x + 200
    # And the total number of spaces in the parking lot is section1_spaces + section2_spaces + section3_spaces
    # Substituting for section2_spaces and section3_spaces, we get:
    # section1_spaces + (x + 200) + x = total_spaces
    # Solving for x, we get:
    x = (total_spaces - section1_spaces - 200) / 2
    section2_spaces = x + 200
    result = section2_spaces
    return result

print(solution())