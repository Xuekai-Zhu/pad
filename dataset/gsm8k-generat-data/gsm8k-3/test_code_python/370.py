def solution():
    """Linda bought two coloring books at $4 each, 4 packs of peanuts at $1.50 each pack, and one stuffed animal. She gave the cashier $25 and got no change. How much does a stuffed animal cost?"""
    # Define the prices of the coloring books and peanuts
    COLORING_BOOK_PRICE = 4
    PEANUTS_PRICE = 1.5

    # Define the number of coloring books and packs of peanuts purchased
    coloring_books = 2
    peanuts_packs = 4

    # Calculate the total cost of the coloring books
    coloring_books_cost = coloring_books * COLORING_BOOK_PRICE

    # Calculate the total cost of the peanuts
    peanuts_cost = peanuts_packs * PEANUTS_PRICE

    # Calculate the cost of the stuffed animal
    stuffed_animal_cost = 25 - coloring_books_cost - peanuts_cost

    # Display the cost of the stuffed animal
    result = stuffed_animal_cost
    return result

print(solution())