def solution():
    """Henry needs to declutter his book collection of 99 books. From his bookshelf, he was able to fill 3 boxes of 15 books each to take to a donation center. He had 21 books in a room he could donate, 4 on his coffee table and 18 cookbooks stashed in the kitchen. When he dropped them off, he noticed a box of books that had a "free to a good home" note. He grabbed 12 books to take back to his place. How many books does Henry now have?"""
    initial_books = 99
    donated_books = 3 * 15 + 21 + 4 + 18
    new_books = 12
    remaining_books = initial_books - donated_books + new_books
    result = remaining_books
    return result

print(solution())