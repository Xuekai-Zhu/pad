def solution():
    total_books = 20  # Beatrice bought 20 books
    first_books = 5  # Beatrice paid $20 for each of the first 5 books
    discount = 2  # Beatrice gets a $2 discount for each additional book over 5

    # Calculate the cost of the first 5 books
    cost_first_books = first_books * 20

    # Calculate the cost of the remaining books
    remaining_books = total_books - first_books
    cost_remaining_books = 0
    for i in range(remaining_books):
        cost_remaining_books += max(20 - (i * discount), 0)

    # Calculate the total cost
    total_cost = cost_first_books + cost_remaining_books
    result = total_cost
    return result

print(solution())