def solution():
    """A group of people contains men, women, and children. The number of men is twice the number of women, and the number of women is 3 times the number of children. If the number of children is 30, how many people does this group contain?"""
    # Define the number of children
    children = 30

    # Calculate the number of women and men
    women = children * 3
    men = women * 2

    # Calculate the total number of people in the group
    total_people = children + women + men

    # return the result
    result = total_people
    return result

print(solution())