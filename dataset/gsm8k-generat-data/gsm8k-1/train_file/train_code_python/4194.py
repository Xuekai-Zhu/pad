def solution():
    """Katy participated in a summer reading program at her local library. She read 8 books in June, twice as many in July and three fewer in August than she did in July. How many books did Katy read during the summer?"""
    
    june_books = 8
    july_books = 2 * june_books
    august_books = july_books - 3
    
    total_books = june_books + july_books + august_books
    
    result = total_books
    return result

print(solution())