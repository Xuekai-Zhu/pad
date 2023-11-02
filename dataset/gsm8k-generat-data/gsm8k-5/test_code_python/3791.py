def solution():
    # Calculate the amount spent on clothes
    clothes_spending = 600 / 2

    # Calculate the amount left after clothes
    left_after_clothes = 600 - clothes_spending

    # Calculate the amount spent on books
    book_spending = left_after_clothes / 2

    # Calculate the amount left after books
    left_after_books = left_after_clothes - book_spending
    result = left_after_books
    return result

print(solution())