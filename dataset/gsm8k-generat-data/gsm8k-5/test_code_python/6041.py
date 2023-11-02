def solution():
    total_books = 145 + 271 + 419 + 209  # Natalia has a total of these many books
    crates_per_nine_books = total_books // 9  # To store 9 books in one crate
    remaining_books = total_books % 9  # Number of books that can't be stored in complete crates
    if remaining_books > 0:
        crates_per_nine_books += 1  # If there are remaining books, then one more crate is needed
    result = crates_per_nine_books
    return result

print(solution())