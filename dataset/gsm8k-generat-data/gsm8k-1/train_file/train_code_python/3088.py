def solution():
    """Tracy has been collecting novels from her friends to donate to the Children For The Future charity organization. In the first week she collects a certain number of books. In the next five weeks, she collects ten times as many books as she did in the first week. How many books did she collect in the first week if she has 99 books now?"""
    total_books = 99
    weeks = 6
    # Let x be the number of books Tracy collects in the first week
    # Then she collects 10x books in the next five weeks
    # Total number of books is x + 10x*5 = 51x
    # Therefore, x = total_books / 51
    first_week_books = total_books / 51
    result = first_week_books
    return result

print(solution())