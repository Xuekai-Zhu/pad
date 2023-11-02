def solution():
    ending_balance = 14
    money_earned = 6

    # Calculate the total amount spent at the movies
    amount_spent = ending_balance - money_earned

    # Calculate the total weekly allowance
    weekly_allowance = amount_spent * 2
    result = weekly_allowance
    return result

print(solution())