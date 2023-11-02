def solution():
    # Calculate Pete's current cash on hand
    cash_on_hand = 2*20 + 4*10

    # Calculate the remaining amount he needs to pay
    remaining_amount = 90 - cash_on_hand

    # Calculate the number of bottles he needs to return
    bottles_needed = remaining_amount / 0.5
    result = bottles_needed
    return result

print(solution())