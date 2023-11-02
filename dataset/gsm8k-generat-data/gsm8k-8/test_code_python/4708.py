def solution():
    starting_balance = 50
    coffee_beans = 10
    tumbler = 30

    amount_spent = coffee_beans + tumbler
    balance_left = starting_balance - amount_spent
    result = balance_left
    return result

print(solution())