def solution():
    # Define the total number of weeks and books read
    total_weeks = 10
    books_per_week = 2
    total_books = total_weeks * books_per_week

    # Calculate how many free donuts Quinn would be eligible for
    donuts_per_5_books = 1
    donuts_earned = total_books // 5 * donuts_per_5_books
    result = donuts_earned
    return result

print(solution())