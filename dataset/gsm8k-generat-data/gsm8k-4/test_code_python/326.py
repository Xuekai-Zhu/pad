def solution():
    """Fred had 236 dollars to spend on 6 books. After buying them, he had 14 dollars. On average, how much did each book cost?"""
    # Define the initial amount of money Fred had
    initial_money = 236

    # Define the amount of money Fred had left after buying the books
    final_money = 14

    # Define the number of books Fred bought
    num_books = 6

    # Calculate the total cost of the books
    total_cost = initial_money - final_money

    # Calculate the average cost per book
    cost_per_book = total_cost / num_books

    result = cost_per_book
    return result

print(solution())