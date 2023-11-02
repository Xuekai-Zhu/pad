def solution():
    """In one hour, Ezra read twice as many books as Ahmed. Ezra has read 300 books this hour and decided to read 150 more. How many books have they read altogether?"""
    ezra_books_per_hour = 2
    ahmed_books_per_hour = 1
    ezra_books_this_hour = 300
    total_books = (ezra_books_per_hour + ahmed_books_per_hour) * (ezra_books_this_hour + 150)
    result = total_books
    return result

print(solution())