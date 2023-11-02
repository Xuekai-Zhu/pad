def solution():
    gift_card = 200  # Marlon has a gift card for $200
    spent_on_monday = gift_card / 2  # Marlon spent half of the gift card on Monday
    remaining_balance = gift_card - spent_on_monday  # Marlon has the remaining balance on Tuesday
    spent_on_tuesday = remaining_balance / 4  # Marlon spent one-fourth of the remaining balance on Tuesday
    balance_left = remaining_balance - spent_on_tuesday  # Marlon has this much left on his gift card

    result = balance_left
    return result

print(solution())