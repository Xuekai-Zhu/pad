def solution():
    initial_amount = 100  # Ian won $100 in the lottery
    colin_payment = 20  # Ian paid $20 to Colin
    helen_payment = colin_payment * 2  # Ian paid twice as much to Helen as he had paid to Colin
    benedict_payment = helen_payment / 2  # Ian paid half as much to Benedict as he had paid to Helen

    # Calculate the total amount Ian paid to his debts
    total_payment = colin_payment + helen_payment + benedict_payment

    # Calculate the amount of money Ian has left after paying off debts
    remaining_amount = initial_amount - total_payment
    result = remaining_amount
    return result

print(solution())