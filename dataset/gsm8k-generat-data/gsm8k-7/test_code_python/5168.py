def solution():
    total_money = 204
    money_spent = total_money / 2

    # Calculate the remaining money after buying the toy
    remaining_money = total_money - money_spent

    # Calculate the money spent on the brother's book
    money_spent_on_book = remaining_money / 2

    # Calculate the money left over
    money_left_over = remaining_money - money_spent_on_book
    result = money_left_over
    return result

print(solution())