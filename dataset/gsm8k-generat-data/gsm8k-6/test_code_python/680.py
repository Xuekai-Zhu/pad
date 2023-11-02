def solution():
    # Calculate the amounts of money Cecil, Catherine, and Carmela have
    cecil_money = 600
    catherine_money = 2 * cecil_money - 250
    carmela_money = 2 * cecil_money + 50

    # Calculate the total amount of money they have together
    total_money = cecil_money + catherine_money + carmela_money
    result = total_money
    return result

print(solution())