def solution():
    """Rick likes to separate his collection of books into various groups by genre.  He has 400 books in total and proceeds to divide them into two separate equally-sized categories repeatedly until he has each book in a category with 24 other books.  How many times must he break these groups into smaller groups to accomplish this?"""
    # Define the target number of books per category
    TARGET_BOOKS_PER_CATEGORY = 24

    # Define the initial number of books
    total_books = 400

    # Define the initial number of categories
    num_categories = 1

    # Divide the books into categories until each category has the target number of books
    while total_books > TARGET_BOOKS_PER_CATEGORY:
        total_books /= 2
        num_categories *= 2

    # Calculate the number of times the groups were divided
    num_divisions = int(math.log2(num_categories))

    # Display the result
    result = num_divisions
    return result

print(solution())