def solution():
    # Calculate the number of pots that cracked
    cracked_pots = (2/5) * 80

    # Calculate the number of pots that did not crack
    remaining_pots = 80 - cracked_pots

    # Calculate the total amount of money Cheyenne made
    total_money = remaining_pots * 40

    result = total_money
    return result

print(solution())