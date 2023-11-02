def solution():
    # Define the number of books read last month
    books_last_month = 4

    # Calculate the goal for this month
    goal_this_month = 2 * books_last_month

    # Calculate the total number of books read for two months
    total_books = books_last_month + goal_this_month
    result = total_books
    return result

print(solution())