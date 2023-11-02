def solution():
    total_books_sold = 15 + 16  # The total number of books sold in January and February
    average_books_per_month = 16  # The average number of books sold per month across all three months
    books_sold_in_march = (average_books_per_month * 3) - total_books_sold  # Calculate the number of books sold in March

    result = books_sold_in_march
    return result

print(solution())