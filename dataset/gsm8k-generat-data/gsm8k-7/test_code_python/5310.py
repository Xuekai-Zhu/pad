def solution():
    words_per_minute = 40
    words_per_page = 100
    num_pages = 80
    total_minutes = 20*60

    # Calculate the total words Sarah can read in the given time
    total_words = words_per_minute * total_minutes

    # Calculate the number of pages she can read in the given time
    total_pages = total_words / words_per_page

    # Calculate the number of books she should check out to cover the total pages
    num_books = total_pages / num_pages
    result = num_books
    return result

print(solution())