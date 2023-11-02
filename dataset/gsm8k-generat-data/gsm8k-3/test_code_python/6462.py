def solution():
    """A book costs $4 more than a CD. The CD is 30% cheaper than a $20 album. How much does the book cost?"""
    # Define the price of the album
    album_price = 20

    # Calculate the price of the CD
    cd_price = album_price - (0.3 * album_price)

    # Calculate the price of the book
    book_price = cd_price + 4

    # Display the price of the book
    result = book_price
    return result

print(solution())