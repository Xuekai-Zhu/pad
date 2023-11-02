def solution():
    """Kay has 14 siblings. Kay is 32 years old. The youngest sibling is 5 less than half Kay's age. The oldest sibling is four times as old as the youngest sibling. How old is the oldest sibling?"""
    # Define the number of siblings and Kay's age
    num_siblings = 14
    kay_age = 32

    # Calculate the age of the youngest sibling
    youngest_sibling = (kay_age / 2) - 5

    # Calculate the age of the oldest sibling
    oldest_sibling = youngest_sibling * 4

    # return the result
    result = oldest_sibling
    return result

print(solution())