def solution():
    initial_money = 30
    loaned_money = 15
    interest_rate = 0.2

    # Calculate the interest on the loaned money
    interest = loaned_money * interest_rate

    # Calculate the total amount Lizzy will have after her friend returns the money
    total_money = initial_money - loaned_money + interest

    result = total_money
    return result

print(solution())