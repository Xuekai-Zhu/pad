def solution():
    """On Tuesday, Mike had 45 books and Corey had twice as many books as Mike. On Wednesday, Mike gave 10 books to Lily, and Corey gave Lily 15 more than Mike gave. How many books did Lily get?"""
    mike_books_tuesday = 45
    corey_books_tuesday = 2 * mike_books_tuesday
    mike_books_wednesday = mike_books_tuesday - 10
    lily_books = mike_books_wednesday + (mike_books_wednesday + 15)
    result = lily_books
    return result

print(solution())