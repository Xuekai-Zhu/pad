def solution():
    initial_amount = 200  # Arthur initially has $200
    spent_amount = (4/5) * initial_amount  # Arthur spends four-fifths of his initial amount
    remaining_amount = initial_amount - spent_amount  # Arthur has the remaining amount left

    result = remaining_amount
    return result

print(solution())