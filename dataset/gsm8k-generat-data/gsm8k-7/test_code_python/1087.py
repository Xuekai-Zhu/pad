def solution():
    num_books_on_shelf = 100
    books_added_after_lunch = 40
    books_remaining_in_evening = 60

    # Calculate the number of books borrowed after lunch
    num_borrowed_after_lunch = num_books_on_shelf - books_remaining_in_evening - books_added_after_lunch

    result = num_borrowed_after_lunch
    return result

print(solution())