def solution():
    house_price = 100000
    down_payment_percent = 0.2
    remaining_balance_percent = 0.7

    # Calculate the amount of the down payment
    down_payment = house_price * down_payment_percent

    # Calculate the remaining balance on the house after the down payment
    remaining_balance = house_price - down_payment

    # Calculate the amount paid by Roger's parents
    parents_payment = remaining_balance * 0.3

    # Calculate the final balance remaining on the house
    final_balance = remaining_balance - parents_payment
    result = final_balance
    return result

print(solution())