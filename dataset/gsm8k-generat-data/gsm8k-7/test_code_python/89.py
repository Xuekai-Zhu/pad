def solution():
    daily_avg = 40
    friday_increase = 0.4

    # Calculate the number of books Krystian borrows on Friday
    friday_books = daily_avg * (1 + friday_increase)

    # Calculate the total number of books borrowed from Monday to Thursday
    mon_thurs_books = daily_avg * 4

    # Calculate the total number of books borrowed in a week
    total_books = mon_thurs_books + friday_books

    result = total_books
    return result

print(solution())