def solution():
    """A 1000 car parking lot is divided into 3 sections. There are 320 spaces in section 1, and 200 more in section 2 than in section 3. How many spaces are made available in section 2 of the parking lot?"""
    total_spaces = 1000
    section1_spaces = 320
    section3_spaces = (total_spaces - section1_spaces) // 3
    section2_spaces = section3_spaces + 200
    result = section2_spaces
    return result

print(solution())