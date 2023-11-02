def solution():
    mom_money = 100
    mildred_spent = 25
    candice_spent = 35

    # Calculate the total amount spent by both Mildred and Candice
    total_spent = mildred_spent + candice_spent

    # Calculate the amount left with them after spending
    amount_left = mom_money - total_spent
    result = amount_left
    return result

print(solution())