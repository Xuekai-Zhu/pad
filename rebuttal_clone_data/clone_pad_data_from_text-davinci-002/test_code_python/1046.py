def solution():
    original_amount = 3 * 12
    amount_given = original_amount / 2
    remaining_amount = original_amount - amount_given
    amount_wilted = remaining_amount / 3
    final_amount = remaining_amount - amount_wilted
    result = final_amount
    return result

print(solution())