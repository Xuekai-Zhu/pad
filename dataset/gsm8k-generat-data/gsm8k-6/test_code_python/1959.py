def solution():
    # Calculate the amount of money Abigail had before losing any
    initial_money = 11 

    # Calculate the amount of money Abigail has after spending $2
    money_after_spending = initial_money - 2 

    # Calculate the amount of money Abigail has lost
    money_lost = money_after_spending - 3 

    result = money_lost
    return result

print(solution())