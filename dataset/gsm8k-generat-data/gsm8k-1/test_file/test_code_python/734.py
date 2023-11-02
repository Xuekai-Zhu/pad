def solution():
    """Alice has 6 more books than Steven. Clara has two times as many books as Steven. If Clara has 20 books, how many more books does Clara have than Alice?"""
    clara_books = 20
    steven_books = clara_books / 2
    alice_books = steven_books - 6
    difference = clara_books - alice_books
    result = difference
    return result

print(solution())