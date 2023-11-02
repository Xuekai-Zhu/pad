def solution():
    # Calculate the total expenses
    total_expenses = 1200 + 400 + 200 + 60 + 200

    # Calculate the amount of money Madeline needs to earn
    money_needed = total_expenses / 0.75 # since she earns $15 per hour, 0.75 of her money is spent on expenses and savings

    # Calculate the number of hours needed to work
    hours_needed = money_needed / 15
    result = hours_needed
    return result

print(solution())