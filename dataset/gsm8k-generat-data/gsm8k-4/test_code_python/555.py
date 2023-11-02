def solution():
    """Jacob has half the number of shoes Edward has. Edward has 3 times the number of shoes Brian has. If Brian has 22 pairs of shoes, how many pairs of shoes do they have in total?"""
    # Define the number of shoes Brian has
    brian_shoes = 22

    # Calculate the number of shoes Edward has
    edward_shoes = brian_shoes * 3

    # Calculate the number of shoes Jacob has
    jacob_shoes = edward_shoes * 0.5

    # Calculate the total number of shoes
    total_shoes = brian_shoes + edward_shoes + jacob_shoes

    # return the result
    result = total_shoes
    return result

print(solution())