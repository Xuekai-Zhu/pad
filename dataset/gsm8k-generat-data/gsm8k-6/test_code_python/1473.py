def solution():
    # Calculate the total number of books sold in three months
    total_books = 15 + 16 + 16*3 - 16*3
    # The average number of books sold per month across all three months is 16
    # Therefore, the total books sold in three months divided by 3 equals 16
    # Solving for the number of books sold in March:
    books_sold_in_march = total_books / 3
    result = books_sold_in_march
    return result

print(solution())