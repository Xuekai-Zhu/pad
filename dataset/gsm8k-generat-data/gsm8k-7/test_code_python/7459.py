def solution():
    initial_payment = 125
    remaining_percentage = 0.75

    # Calculate the original amount owed
    original_amount = initial_payment / (1 - remaining_percentage)
    result = original_amount
    return result

print(solution())