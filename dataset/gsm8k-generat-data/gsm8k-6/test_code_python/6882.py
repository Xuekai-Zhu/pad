def solution():
    # Calculate the amount of money Brendan has left after buying the car
    remaining_money = 5000 - 1500

    # Calculate the amount of money he recharges his debit card with every week
    recharge_amount = 0.5 * remaining_money

    # Calculate the amount of money he has left at the end of June, assuming he is paid weekly
    remaining_money = remaining_money + (4 * recharge_amount)

    result = remaining_money
    return result

print(solution())