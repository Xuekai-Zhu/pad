def solution():
    """Rick likes to separate his collection of books into various groups by genre. He has 400 books in total and proceeds to divide them into two separate equally-sized categories repeatedly until he has each book in a category with 24 other books. How many times must he break these groups into smaller groups to accomplish this?"""
    # Define the initial number of books and the target size of each category
    books = 400
    target_size = 24

    # Initialize the counter for the number of divisions
    divisions = 0

    # Divide the books into two equally-sized categories until each category has the target size
    while books > target_size:
        books /= 2
        divisions += 1

    # Return the result
    result = divisions
    return result

print(solution())