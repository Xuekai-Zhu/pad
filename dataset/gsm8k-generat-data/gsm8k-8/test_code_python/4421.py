def solution():
    patricia_money = 6
    lisa_money = 5 * patricia_money
    charlotte_money = lisa_money / 2

    total_money = patricia_money + lisa_money + charlotte_money

    additional_money_needed = 100 - total_money
    result = additional_money_needed
    return result

print(solution())