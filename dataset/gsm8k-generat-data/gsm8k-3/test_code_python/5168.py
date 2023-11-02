def solution():
    """Isabel has $204 in her piggy bank. She spent half the amount and bought a toy. She then spent half of the remaining money and bought her brother a book. How much money, in dollars, was left over?"""
    # Calculate the amount Isabel spent on the toy
    toy_cost = 204/2

    # Calculate the amount of money Isabel had left after buying the toy
    remaining_money = 204 - toy_cost

    # Calculate the amount Isabel spent on the book
    book_cost = remaining_money/2

    # Calculate the amount of money Isabel had left after buying the book
    left_over_money = remaining_money - book_cost

    # Display the amount of money left over
    result = left_over_money
    return result

print(solution())