def solution():
    # Calculate the total amount of money Asha has
    total_money = 20 + 40 + 30 + 70 + 100  # borrowed money and savings
    spent_money = (3/4) * total_money  # amount spent

    # Calculate the remaining money after spending
    remaining_money = total_money - spent_money
    result = remaining_money
    return result

print(solution())