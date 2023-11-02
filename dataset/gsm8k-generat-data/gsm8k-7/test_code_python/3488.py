def solution():
    num_books_two_years_ago = 200
    num_books_now = num_books_two_years_ago - 40

    num_books_in_five_years = 60 + 5*num_books_now

    total_num_books = num_books_now + num_books_in_five_years

    result = total_num_books
    return result

print(solution())