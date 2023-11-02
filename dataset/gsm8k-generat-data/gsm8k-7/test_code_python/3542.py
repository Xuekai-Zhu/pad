def solution():
    num_books = 3
    cost_per_day = 0.5
    book1_days = 20
    book2_days = 31
    book3_days = 31

    # Calculate the total cost for book 1
    book1_cost = book1_days * cost_per_day

    # Calculate the total cost for book 2
    book2_cost = book2_days * cost_per_day

    # Calculate the total cost for book 3
    book3_cost = book3_days * cost_per_day

    # Calculate the total cost for all books
    total_cost = book1_cost + book2_cost + book3_cost
    result = total_cost
    return result

print(solution())