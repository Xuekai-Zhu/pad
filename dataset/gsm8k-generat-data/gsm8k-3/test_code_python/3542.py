def solution():
    """A book library charges fifty cents per day on any book borrowed by its members to read outside the library's premises. At the start of May, Celine borrowed three books from the library to read at home for her upcoming examinations. If she returned one book 20 days after borrowing it, and the other two stayed at her house until the end of May, calculate the total amount of money that she paid at the library for lending the three books."""
    # Define the cost per day for borrowing a book
    COST_PER_DAY = 0.5

    # Define the number of days each book was borrowed
    book1_days = 20
    book2_days = 31
    book3_days = 31

    # Calculate the total cost for borrowing the three books
    book1_cost = book1_days * COST_PER_DAY
    book2_cost = book2_days * COST_PER_DAY
    book3_cost = book3_days * COST_PER_DAY

    total_cost = book1_cost + book2_cost + book3_cost

    # Display the total cost
    result = total_cost
    return result

print(solution())