def solution():
    """Tracy has been collecting novels from her friends to donate to the Children For The Future charity organization. In the first week she collects a certain number of books. In the next five weeks, she collects ten times as many books as she did in the first week. How many books did she collect in the first week if she has 99 books now?"""
    # Define the number of books collected in the first week as x
    x = None

    # Calculate the number of books collected in the next five weeks as 10x
    y = 10 * x

    # Calculate the total number of books collected as x + y
    total_books = x + y

    # If total_books = 99, then solve for x
    # 99 = x + 10x
    # 99 = 11x
    # x = 9
    x = 9

    # Return the result
    result = x
    return result

print(solution())