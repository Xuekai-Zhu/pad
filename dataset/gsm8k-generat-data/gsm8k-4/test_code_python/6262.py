def solution():
    """The ratio of books to pens that Arlo has to buy for his school supplies is 7:3. If he bought a total of 400 stationery from the store, calculate the number of books he bought."""
    # Define the ratio of books to pens
    book_to_pen_ratio = 7 / 3

    # Calculate the total number of items purchased
    total_items = 400

    # Calculate the number of items per unit of the ratio
    unit_items = total_items / (7 + 3)

    # Calculate the number of books purchased
    books = book_to_pen_ratio * unit_items

    result = books
    return result

print(solution())