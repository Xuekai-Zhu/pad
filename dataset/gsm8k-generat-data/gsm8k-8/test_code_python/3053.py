def solution():
    # Calculate the total savings after 6 weeks
    total_savings = 25 * 6

    # Calculate the amount used to pay bills
    bills_payment = total_savings / 3

    # Calculate the remaining savings after bills payment
    remaining_savings = total_savings - bills_payment

    # Calculate the amount needed for the coat
    coat_cost = 170

    # Calculate the extra money Carl needs from his dad
    extra_money = coat_cost - remaining_savings

    result = extra_money
    return result

print(solution())