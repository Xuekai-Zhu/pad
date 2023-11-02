def solution():
    giftcard_balance = 200
    monday_spending = giftcard_balance / 2
    remainder_balance = giftcard_balance - monday_spending
    tuesday_spending = remainder_balance / 4
    remaining_balance = remainder_balance - tuesday_spending
    result = remaining_balance
    return result

print(solution())