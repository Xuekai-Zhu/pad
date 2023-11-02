def solution():
    """There are 250 books inside a library. On Tuesday, 120 books are taken out to be read by children. On Wednesday, 35 books are returned. On Thursday, another 15 books are withdrawn from the library. How many books are now in the library?"""
    total_books = 250
    tuesday_taken = 120
    wednesday_returned = 35
    thursday_taken = 15
    remaining_books = total_books - tuesday_taken + wednesday_returned - thursday_taken
    result = remaining_books
    return result

print(solution())