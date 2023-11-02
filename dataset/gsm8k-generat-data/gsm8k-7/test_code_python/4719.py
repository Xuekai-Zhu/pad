def solution():
    original_money = 48
    snacks_spending = 8
    remaining_money = original_money - snacks_spending

    # Calculate the remaining money after spending on computer accessories
    remaining_money = remaining_money - 0.5*original_money + 4

    # Calculate the spending on computer accessories
    computer_accessories_spending = original_money - remaining_money - snacks_spending
    result = computer_accessories_spending
    return result

print(solution())