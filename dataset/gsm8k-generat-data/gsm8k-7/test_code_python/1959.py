def solution():
    start_money = 11
    spent_money = 2
    remaining_money = 3

    # Calculate the total amount of money Abigail had before losing any
    total_money_before_loss = start_money - spent_money

    # Calculate the amount of money Abigail has lost
    lost_money = total_money_before_loss - remaining_money
    result = lost_money
    return result

print(solution())