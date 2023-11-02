def solution():
    starting_money = 11  # Abigail had $11 in her purse at the start of the day
    money_spent = 2  # Abigail spent $2 in a store
    remaining_money = 3  # Abigail has $3 left in her purse

    # Calculate how much money Abigail had before she lost some
    total_money_before_loss = starting_money - money_spent

    # Calculate how much money Abigail has lost
    money_lost = total_money_before_loss - remaining_money
    result = money_lost
    return result

print(solution())