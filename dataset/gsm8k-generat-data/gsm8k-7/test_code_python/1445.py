def solution():
    num_books = 3
    total_days = 10
    words_per_hour = 100
    book_words = [200, 400, 300]

    # Calculate the total number of words that Jenny needs to read
    total_words = sum(book_words)

    # Calculate the number of hours Jenny needs to spend reading
    total_hours = total_words / words_per_hour

    # Calculate the number of minutes per day that Jenny needs to spend reading
    minutes_per_day = (total_hours / total_days) * 60
    result = minutes_per_day
    return result

print(solution())