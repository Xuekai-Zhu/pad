def solution():
    initial_balance = 50
    coffee_cost = 10
    tumbler_cost = 30

    # Calculate the total amount spent
    total_spent = coffee_cost + tumbler_cost

    # Calculate the remaining balance
    remaining_balance = initial_balance - total_spent
    result = remaining_balance
    return result

print(solution())