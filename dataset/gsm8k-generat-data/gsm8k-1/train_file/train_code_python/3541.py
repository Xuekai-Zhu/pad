def solution():
    """A book library charges fifty cents per day on any book borrowed by its members to read outside the library's premises. At the start of May, Celine borrowed three books from the library to read at home for her upcoming examinations. If she returned one book 20 days after borrowing it, and the other two stayed at her house until the end of May, calculate the total amount of money that she paid at the library for lending the three books."""
    num_books = 3
    days_book1 = 20
    days_book2 = 31
    days_book3 = 31
    fine_per_day = 0.5
    total_fine_book1 = days_book1 * fine_per_day
    total_fine_book2 = days_book2 * fine_per_day
    total_fine_book3 = days_book3 * fine_per_day
    total_fine = total_fine_book1 + total_fine_book2 + total_fine_book3
    result = total_fine
    return result

print(solution())