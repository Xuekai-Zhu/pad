def solution():
    
    initial_balance = 50
    first_interest = initial_balance * 0.2
    first_balance = initial_balance + first_interest

    second_balance = first_balance + 20
    second_interest = second_balance * 0.2
    final_balance = second_balance + second_interest

    result = final_balance
    return result

print(solution())