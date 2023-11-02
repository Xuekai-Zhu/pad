def solution():
    """There are 35 books on the cart. There are five fiction books, 4 more non-fiction books than fiction books, 2 times as many autobiographies as fiction books, and the rest picture books. How many books were picture books?"""
    # Define the number of fiction books
    fiction = 5

    # Calculate the number of non-fiction books
    non_fiction = fiction + 4

    # Calculate the number of autobiographies
    autobiographies = fiction * 2

    # Calculate the total number of fiction, non-fiction, and autobiography books
    total = fiction + non_fiction + autobiographies

    # Calculate the number of picture books
    picture_books = 35 - total

    # Display the number of picture books
    result = picture_books
    return result

print(solution())