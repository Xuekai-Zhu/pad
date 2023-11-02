def solution():
    initial_cost = 100000
    down_payment = initial_cost * .2
    additional_payment = initial_cost * .3
    remaining_balance = initial_cost - down_payment - additional_payment
    result = remaining_balance
    return result

print(solution())