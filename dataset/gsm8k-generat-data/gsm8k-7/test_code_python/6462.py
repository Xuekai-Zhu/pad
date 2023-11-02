def solution():
    album_price = 20

    # Calculate the price of the CD
    cd_price = album_price * 0.7

    # Calculate the price difference between the book and CD
    price_difference = 4

    # Calculate the price of the book
    book_price = cd_price + price_difference
    result = book_price
    return result

print(solution())