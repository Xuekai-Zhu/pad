def solution():
    """Javier has a wife and 3 children. They have 2 dogs and 1 cat. Including Javier, how many legs are there in total in Javier’s household?"""
    # Define the number of legs for each member of the household
    javier_legs = 2
    wife_legs = 2
    child_legs = 2
    dog_legs = 4
    cat_legs = 4

    # Calculate the total number of legs
    total_legs = javier_legs + wife_legs + (3 * child_legs) + (2 * dog_legs) + cat_legs

    result = total_legs
    return result

print(solution())