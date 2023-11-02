def solution():
    gift_card = 200
    spent_on_monday = gift_card / 2
    remaining_balance = gift_card - spent_on_monday
    spent_on_tuesday = remaining_balance / 4
    balance_after_tuesday = remaining_balance - spent_on_tuesday
    result = balance_after_tuesday
    return result

print(solution())