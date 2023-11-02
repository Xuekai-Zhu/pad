def solution():
    ending_balance = 14  # Fred ended with 14 dollars
    money_earned = 6  # Fred earned 6 dollars washing the family car

    # Calculate the amount Fred spent on the movies
    money_spent = (ending_balance - money_earned) / 2

    # Calculate Fred's weekly allowance
    weekly_allowance = money_earned + money_spent
    result = weekly_allowance
    return result

print(solution())