def solution():
    card_price = 100

    patricia_money = 6
    lisa_money = 5 * patricia_money
    charlotte_money = lisa_money / 2

    total_money = patricia_money + lisa_money + charlotte_money

    remaining_money_needed = card_price - total_money
    result = remaining_money_needed
    return result

print(solution())