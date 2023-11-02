def solution():
    initial_amount = 204
    spent_on_toy = initial_amount / 2
    remaining_amount = initial_amount - spent_on_toy
    spent_on_book = remaining_amount / 2
    final_amount = remaining_amount - spent_on_book
    result = final_amount  # final amount of money left over
    return result

print(solution())