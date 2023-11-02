def solution():
    # Lorie starts with 2 pieces of $100 bills
    total_amount = 200

    # She changes one piece of the $100 bill into $50 bills
    total_amount += 50 * 100

    # Half of the remaining $100 bill is changed to $10 bills
    remaining_amount = total_amount - 100
    total_amount += (remaining_amount / 2) * 10

    # The rest of the remaining $100 bill is changed to $5 bills
    remaining_amount -= (remaining_amount / 2) * 10
    total_amount += (remaining_amount / 5) * 5

    # Calculate the total number of pieces of bills Lorie has
    total_pieces = total_amount / 100

    result = total_pieces
    return result

print(solution())