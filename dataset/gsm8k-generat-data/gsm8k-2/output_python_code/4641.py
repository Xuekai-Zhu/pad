def solution():
    """Mcgregor and Floyd were assigned 89 books to read for the week. If Mcgregor was able to finish 34 while Floyd was able to finish 32, how many books do they still have to read?"""
    total_books = 89
    mcgregor_books = 34
    floyd_books = 32
    remaining_books = total_books - mcgregor_books - floyd_books
    result = remaining_books
    return result

print(solution())