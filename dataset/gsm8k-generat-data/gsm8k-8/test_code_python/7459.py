def solution():
    # Define the initial installment and the remaining amount to be paid
    initial_payment = 125
    remaining_amount = 0.75

    # Calculate the total amount owed by dividing the remaining amount by the percentage (0.75 = 75%)
    total_owed = initial_payment / (1 - remaining_amount)
    result = total_owed
    return result

print(solution())