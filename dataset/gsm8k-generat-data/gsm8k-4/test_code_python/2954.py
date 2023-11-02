def solution():
    """A 1000 car parking lot is divided into 3 sections. There are 320 spaces in section 1, and 200 more in section 2 than in section 3. How many spaces are made available in section 2 of the parking lot?"""
    # Define the total number of spaces in the parking lot
    total_spaces = 1000

    # Define the number of spaces in section 1
    section1_spaces = 320

    # Define the number of spaces in section 3
    section3_spaces = (total_spaces - section1_spaces) / 2

    # Define the number of spaces in section 2
    section2_spaces = section3_spaces + 200

    result = section2_spaces
    return result

print(solution())