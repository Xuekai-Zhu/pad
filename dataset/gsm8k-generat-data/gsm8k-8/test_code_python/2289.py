def solution():
    # Calculate the cost of the first two books with the discount
    discounted_books_cost = (13 + 15) * 0.75

    # Calculate the total cost of all four books
    total_books_cost = discounted_books_cost + 10 + 10

    # Calculate the amount needed to spend to qualify for free shipping
    amount_needed = 50 - total_books_cost

    result = amount_needed
    return result

print(solution())