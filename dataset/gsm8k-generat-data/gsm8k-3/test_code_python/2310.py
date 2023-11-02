def solution():
    """Selena reads a book with 400 pages. Harry reads a book with 20 fewer than half the number of pages Selena's book has. How many pages are in the book of Harry?"""
    # Selena's book
    selena_pages = 400

    # Harry's book
    harry_pages = (selena_pages / 2) - 20

    # Display the number of pages in Harry's book
    result = harry_pages
    return result

print(solution())