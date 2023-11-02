def solution():
    # Calculate the amount of the tip
    tip = 0.2 * 200

    # Calculate the total amount to be paid
    total_amount = 200 + tip + 10

    # Calculate the amount Mark needs to add
    mark_add = total_amount - (200 + tip)
    result = mark_add
    return result

print(solution())