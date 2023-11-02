def solution():
    remaining_money_after_groceries = 4/5  # 1 - 1/5
    remaining_money_after_magazine = 3/4  # 1 - 1/4
    final_money = 360

    # Calculate the money Frank had after buying groceries
    money_after_groceries = final_money / remaining_money_after_magazine

    # Calculate the money Frank had initially
    initial_money = money_after_groceries / remaining_money_after_groceries
    result = initial_money
    return result

print(solution())