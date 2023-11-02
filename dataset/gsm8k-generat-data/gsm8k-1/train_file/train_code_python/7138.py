def solution():
    """Rick likes to separate his collection of books into various groups by genre. He has 400 books in total and proceeds to divide them into two separate equally-sized categories repeatedly until he has each book in a category with 24 other books. How many times must he break these groups into smaller groups to accomplish this?"""
    total_books = 400
    final_size = 24
    current_size = total_books
    count = 0
    while current_size > final_size:
        current_size /= 2
        count += 1
    result = count
    return result

print(solution())