def solution():
    initial_money_in_cents = 85  # $0.85 is 85 cents
    money_from_mother_in_cents = 40  # $0.40 is 40 cents
    money_found_in_cents = 50  # $0.50 is 50 cents
    cost_of_toy_in_cents = 160  # $1.60 is 160 cents

    # Calculate the total amount of money Yanni has in cents
    total_money_in_cents = initial_money_in_cents + money_from_mother_in_cents + money_found_in_cents

    # Calculate the amount of money Yanni has left in cents
    money_left_in_cents = total_money_in_cents - cost_of_toy_in_cents
    result = money_left_in_cents
    return result

print(solution())