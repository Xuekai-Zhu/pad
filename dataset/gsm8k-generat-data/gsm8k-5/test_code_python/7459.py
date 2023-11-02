def solution():
    initial_installment = 125  # Mathilda pays an initial installment of $125
    remaining_percentage = 0.75  # Mathilda still has 75% left to pay
    remaining_amount = initial_installment / (1 - remaining_percentage)  # Calculate the remaining amount that Mathilda owes

    # Calculate the original amount that Mathilda owed
    original_amount = remaining_amount + initial_installment
    result = original_amount
    return result

print(solution())