def solution():
    """Ian had twenty roses. He gave six roses to his mother, nine roses to his grandmother, four roses to his sister, and he kept the rest. How many roses did Ian keep?"""
    # Define the initial number of roses
    initial_roses = 20

    # Calculate the number of roses given to Ian's mother, grandmother, and sister
    given_roses = 6 + 9 + 4

    # Calculate the number of roses Ian kept
    kept_roses = initial_roses - given_roses

    # return the result
    result = kept_roses
    return result

print(solution())