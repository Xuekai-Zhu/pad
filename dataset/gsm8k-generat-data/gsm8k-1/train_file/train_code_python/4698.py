def solution():
    """Carlos read 28 books in July and 30 books in August. He needed to read 100 books during his summer vacation. If Carlos read some of the books in June, calculate the number of books that Carlos read in June to meet his goal?"""
    books_goal = 100
    books_read = 28 + 30
    books_june = books_goal - books_read
    result = books_june
    return result

print(solution())