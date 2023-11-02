def solution():
    # Calculate the number of spaces in section 3
    spaces_section3 = (1000 - 320) / 2  # divide remaining spaces equally between section 2 and section 3
    # Calculate the number of spaces in section 2
    spaces_section2 = spaces_section3 + 200
    result = spaces_section2
    return result

print(solution())