def solution():
    """A 1000 car parking lot is divided into 3 sections. There are 320 spaces in section 1, and 200 more in section 2 than in section 3. How many spaces are made available in section 2 of the parking lot?"""
    # Define the number of spaces in section 1
    section_1 = 320

    # Define the difference in spaces between section 2 and section 3
    difference = 200

    # Calculate the total number of spaces in section 2 and section 3
    total_spaces = 1000 - section_1
    # Let x be the number of spaces in section 3
    # Then the number of spaces in section 2 is x + 200
    # We know that the total spaces in section 2 and 3 is equal to total_spaces
    # So we can set up the equation x + (x + 200) = total_spaces and solve for x
    x = (total_spaces - 200) / 2
    section_3 = x
    section_2 = x + 200

    # Display the number of spaces in section 2
    result = section_2
    return result

print(solution())