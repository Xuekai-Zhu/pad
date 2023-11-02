def solution():
    mom_cup_size = 8
    mom_tea_amount = 1
    party_size = 12
    cup_size = 6

    # Calculate the total amount of tea needed for the party
    total_cup_size = party_size * cup_size
    total_tea_amount = total_cup_size / mom_cup_size * mom_tea_amount
    result = total_tea_amount
    return result

print(solution())