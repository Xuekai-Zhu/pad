def solution():
    # Calculate the amount of money Randy kept
    start_amount = 3000  # Randy's starting amount
    added_amount = 200  # amount added by Smith
    amount_spent = 1200  # amount given to Sally
    amount_kept = start_amount + added_amount - amount_spent
    result = amount_kept
    return result

print(solution())