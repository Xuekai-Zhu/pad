def solution():
    """Amy is building 2 3 ft long by 3 ft wide garden beds and 2 4ft long by 3 ft wide garden beds. What is the total sq ft of growing space that she will have?"""
    # Define the dimensions of the garden beds
    beds = [(3,3), (4,3), (3,3), (4,3)]

    # Calculate the total square footage of growing space
    total_sq_ft = sum([l*w for l,w in beds])

    # return the result
    result = total_sq_ft
    return result

print(solution())