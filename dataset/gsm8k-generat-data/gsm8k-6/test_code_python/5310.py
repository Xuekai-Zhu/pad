def solution():
    # Calculate the total number of words Sarah will read
    total_words = 100 * 80 * 60 * 20  # 100 words per page, 80 pages per book, 60 minutes per hour, 20 hours of reading

    # Calculate the number of books Sarah should check out
    books_needed = total_words / (40 * 60 * 20)  # 40 words per minute, 60 minutes per hour, 20 hours of reading

    result = round(books_needed)  # round up to the nearest book
    return result

print(solution())