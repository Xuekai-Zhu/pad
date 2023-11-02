def solution():
    """The ratio of books to pens that Arlo has to buy for his school supplies is 7:3. If he bought a total of 400 stationery from the store, calculate the number of books he bought."""
    # Define the ratio of books to pens
    BOOKS_TO_PENS = 7/3

    # Define the total number of stationery purchased
    total_stationery = 400

    # Calculate the number of books purchased
    num_books = total_stationery / (BOOKS_TO_PENS + 1)

    # Display the number of books purchased
    result = num_books
    return result

print(solution())