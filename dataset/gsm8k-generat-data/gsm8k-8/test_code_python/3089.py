def solution():
    total_books = 99
    num_weeks = 6
    books_per_week = [0] * num_weeks
    books_per_week[0] = x  # Let's assume the unknown number of books she collected in the first week is x
    books_per_week[1] = 10 * books_per_week[0]  # She collected ten times as many books in the second week
    books_per_week[2:6] = [10 * books_per_week[1]] * 4  # She collected ten times as many books in each of the last four weeks
    
    total_books_collected = sum(books_per_week)
    result = x
    return result

print(solution())