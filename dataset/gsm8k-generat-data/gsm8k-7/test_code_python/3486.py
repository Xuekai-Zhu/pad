def solution():
    smith_money = 200
    sally_money = 1200
    total_money_left = 2000

    # Calculate the total amount of money Randy had after Smith gave him money
    total_money_after_smith = total_money_left + sally_money

    # Calculate the amount of money Randy had before giving money to Sally
    initial_money = total_money_after_smith - smith_money
    result = initial_money
    return result

print(solution())