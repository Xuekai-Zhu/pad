def solution():
    """A group of people contains men, women, and children. The number of men is twice the number of women, and the number of women is 3 times the number of children. If the number of children is 30, how many people does this group contain?"""
    # Define the number of children
    children = 30

    # Calculate the number of women
    women = children * 3

    # Calculate the number of men
    men = women * 2

    # Calculate the total number of people
    total_people = children + women + men

    # Display the total number of people
    result = total_people
    return result

print(solution())