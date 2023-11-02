def solution():
    num_books = 8
    book_price = 5
    current_savings = 13

    # Calculate the total cost of all 8 books
    total_cost = num_books * book_price

    # Calculate the amount of money that Tommy needs to save up
    needed_savings = total_cost - current_savings
    result = needed_savings
    return result

print(solution())