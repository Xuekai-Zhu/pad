def solution():
    """A book library charges fifty cents per day on any book borrowed by its members to read outside the library's premises. At the start of May, Celine borrowed three books from the library to read at home for her upcoming examinations. If she returned one book 20 days after borrowing it, and the other two stayed at her house until the end of May, calculate the total amount of money that she paid at the library for lending the three books."""
    days_late_book1 = 20
    days_late_books2and3 = 31 #assuming May has 31 days
    late_charges_book1 = 0.5 * days_late_book1
    late_charges_books2and3 = 0.5 * days_late_books2and3 * 2
    total_charges = late_charges_book1 + late_charges_books2and3
    result = total_charges
    return result

print(solution())