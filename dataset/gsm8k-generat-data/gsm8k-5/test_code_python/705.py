def solution():
    amount_left = 51  # Isabel has $51 left after buying the toy and book
    amount_spent_on_book = amount_left * 0.5  # Isabel spent half of the remaining money on the book
    amount_spent_on_toy = amount_spent_on_book * 2  # Isabel spent half of the original amount on the toy

    # Calculate the original amount of money Isabel had in her piggy bank
    original_amount = amount_left + amount_spent_on_book + amount_spent_on_toy
    result = original_amount
    return result

print(solution())