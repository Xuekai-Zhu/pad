def solution():
    """Rick likes to separate his collection of books into various groups by genre. He has 400 books in total and proceeds to divide them into two separate equally-sized categories repeatedly until he has each book in a category with 24 other books. How many times must he break these groups into smaller groups to accomplish this?"""
    num_books = 400
    final_group_size = 24
    current_group_size = num_books / 2
    num_divisions = 0
    while current_group_size != final_group_size:
        current_group_size /= 2
        num_divisions += 1
    result = num_divisions
    return result

print(solution())