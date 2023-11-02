def solution():
    starting_balance = 125
    increase = 0.25
    decrease = 0.2

    # Calculate the balance after the increase
    balance_after_increase = starting_balance + (increase * starting_balance)

    # Calculate the balance after the decrease
    balance_after_decrease = balance_after_increase - (decrease * balance_after_increase)

    # Calculate the final balance as a percentage of the starting balance
    final_balance_percentage = (balance_after_decrease / starting_balance) * 100
    result = final_balance_percentage
    return result

print(solution())