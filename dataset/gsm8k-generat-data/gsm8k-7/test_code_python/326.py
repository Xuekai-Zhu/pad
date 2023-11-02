def solution():
    initial_amount = 236
    final_amount = 14
    num_books = 6

    # Calculate the total amount spent on the books
    total_spent = initial_amount - final_amount

    # Calculate the average cost per book
    avg_cost = total_spent / num_books
    result = avg_cost
    return result

print(solution())