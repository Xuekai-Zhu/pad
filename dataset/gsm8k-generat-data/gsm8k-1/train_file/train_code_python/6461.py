def solution():
    """A book costs $4 more than a CD. The CD is 30% cheaper than a $20 album. How much does the book cost?"""
    album_price = 20
    cd_price = album_price * 0.7
    book_price = cd_price + 4
    result = book_price
    return result

print(solution())