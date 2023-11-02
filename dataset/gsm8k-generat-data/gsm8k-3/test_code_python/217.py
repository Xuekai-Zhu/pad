def solution():
    """A church has 120 members. 40% are adults. The rest are children. How many more children are there than adults?"""
    # Define the total number of members
    total_members = 120

    # Calculate the number of adult members
    adult_members = total_members * 0.4

    # Calculate the number of child members
    child_members = total_members - adult_members

    # Calculate the difference between the number of child and adult members
    difference = child_members - adult_members

    # Display the difference
    result = difference
    return result

print(solution())