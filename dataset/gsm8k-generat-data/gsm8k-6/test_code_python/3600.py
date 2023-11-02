def solution():
    # Calculate the length of the portion of Pat's stick that is not covered in dirt
    uncovered_length = 30 - 7 

    # Calculate the length of Sarah's stick
    sarah_length = uncovered_length * 2 

    # Calculate the length of Jane's stick in inches
    jane_length = sarah_length - (2 * 12)  # convert 2 feet to 24 inches

    result = jane_length
    return result

print(solution())