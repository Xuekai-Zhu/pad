def solution():
    initial_balance = 65
    deposit = 15
    withdrawal = 4

    # Calculate Lucy's new balance after deposit
    new_balance = initial_balance + deposit

    # Calculate Lucy's final balance after withdrawal
    final_balance = new_balance - withdrawal
    result = final_balance
    return result

print(solution())