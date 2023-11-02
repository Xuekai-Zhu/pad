def solution():
    """Isabel has $204 in her piggy bank. She spent half the amount and bought a toy. She then spent half of the remaining money and bought her brother a book. How much money, in dollars, was left over?"""
    # Define the initial amount of money
    initial_amount = 204

    # Calculate the amount of money spent on the toy
    toy_cost = initial_amount / 2

    # Calculate the remaining amount of money
    remaining_amount = initial_amount - toy_cost

    # Calculate the amount of money spent on the book
    book_cost = remaining_amount / 2

    # Calculate the amount of money left over
    left_over = remaining_amount - book_cost

    # Return the result
    result = left_over
    return result

print(solution())