def solution():
    """A book library charges fifty cents per day on any book borrowed by its members to read outside the library's premises. At the start of May, Celine borrowed three books from the library to read at home for her upcoming examinations. If she returned one book 20 days after borrowing it, and the other two stayed at her house until the end of May, calculate the total amount of money that she paid at the library for lending the three books."""
    # Define the daily charge for borrowing a book
    daily_charge = 0.5

    # Define the number of books borrowed by Celine
    num_books = 3

    # Define the number of days each book was borrowed
    days_book1 = 20
    days_book2 = 31
    days_book3 = 31

    # Calculate the total amount paid by Celine for borrowing the books
    total_charge = daily_charge * (days_book1 + days_book2 + days_book3)

    # return the result
    result = total_charge
    return result

print(solution())