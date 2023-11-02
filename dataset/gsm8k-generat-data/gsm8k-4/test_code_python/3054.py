def solution():
    """John has 10 members of his family on his father's side. His mother's side is 30% larger. How many people are there in total?"""
    # Define the number of members on John's father's side
    father_members = 10

    # Calculate the 30% increase for John's mother's side
    mother_increase = 0.30 * father_members

    # Calculate the new number of members on John's mother's side
    mother_members = father_members + mother_increase

    # Calculate the total number of family members
    total_members = father_members + mother_members

    # return the result
    result = total_members
    return result

print(solution())