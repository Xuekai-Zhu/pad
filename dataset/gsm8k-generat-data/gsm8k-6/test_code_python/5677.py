def solution():
    # Calculate the time it takes Tom to type 10 pages
    words_per_page = 450
    pages = 10
    words = words_per_page * pages
    time_in_minutes = words / 90
    result = time_in_minutes
    return result

print(solution())