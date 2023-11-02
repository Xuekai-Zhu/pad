def solution():
    # Define the initial house cost and down payment
    house_cost = 100000
    down_payment = 0.2 * house_cost

    # Calculate the remaining balance after down payment
    remaining_balance = house_cost - down_payment

    # Calculate the amount paid off by Roger's parents
    parent_payment = 0.3 * remaining_balance

    # Calculate the final balance still owed by Roger
    final_balance = remaining_balance - parent_payment

    result = final_balance
    return result

print(solution())