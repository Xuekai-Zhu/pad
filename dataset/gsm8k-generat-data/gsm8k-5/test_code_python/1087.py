def solution():
    total_books = 100  # Hadley arranges 100 books on the shelf
    added_books = 40  # Hadley adds 40 more books to the shelf
    remaining_books = 60  # Hadley sees that there are 60 books remaining on the shelf in the evening

    # Calculate how many books were borrowed before evening
    borrowed_books = total_books + added_books - remaining_books

    # Calculate how many of those books were borrowed by lunchtime
    borrowed_by_lunchtime = borrowed_books - 30
    result = borrowed_by_lunchtime
    return result

print(solution())