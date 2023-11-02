def solution():
    """A church has 120 members. 40% are adults. The rest are children. How many more children are there than adults?"""
    # Define the total number of members
    total_members = 120

    # Calculate the number of adult members
    adult_members = total_members * 0.4

    # Calculate the number of children members
    children_members = total_members - adult_members

    # Calculate the difference between the number of children and adult members
    difference = children_members - adult_members
    
    # return the result
    result = abs(difference)
    return result

print(solution())