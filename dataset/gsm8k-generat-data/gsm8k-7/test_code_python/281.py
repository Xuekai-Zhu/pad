def solution():
    betty_balance = 3456
    gina_balance = betty_balance / 4  # Calculate the balance in one of Gina's accounts
    total_balance = (2 * gina_balance) + betty_balance  # Calculate the combined balance
    result = total_balance
    return result

print(solution())