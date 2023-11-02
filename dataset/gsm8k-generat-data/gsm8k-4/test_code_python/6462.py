def solution():
    """A book costs $4 more than a CD. The CD is 30% cheaper than a $20 album. How much does the book cost?"""
    # Define the price of the album
    album_price = 20
    
    # Calculate the price of the CD
    cd_price = album_price * 0.7
    
    # Calculate the price of the book
    book_price = cd_price + 4
    
    # Round the result to two decimal places
    result = round(book_price, 2)
    return result

print(solution())