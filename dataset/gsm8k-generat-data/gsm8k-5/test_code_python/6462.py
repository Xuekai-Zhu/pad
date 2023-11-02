def solution():
    album_price = 20  # The album costs $20
    cd_price = album_price * 0.7  # The CD is 30% cheaper than the album
    book_price = cd_price + 4  # The book costs $4 more than the CD

    result = book_price
    return result

print(solution())