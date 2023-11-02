def solution():
    """Lidia has a collection of books. Her collection is four times bigger than the collection which her friend Susan has. In total Susan and Lidia, both have 3000 books. How many books does Susan have in her collection?"""
    total_books = 3000
    lidia_books = total_books / 5 # Lidia has 4 times more books than Susan
    susan_books = total_books - lidia_books
    result = susan_books
    return result

print(solution())