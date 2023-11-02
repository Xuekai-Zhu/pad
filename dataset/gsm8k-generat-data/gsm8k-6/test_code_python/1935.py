def solution():
    # Calculate the total amount of money Reese had in her savings account initially
    remaining_amount = 2900  # remaining amount in April
    amount_spent_april = 1500  # amount spent in April
    amount_spent_march = 0.4 * (remaining_amount + amount_spent_april)  # amount spent in March
    total_spent = 0.2 * remaining_amount + amount_spent_march  # total amount spent in February and March
    initial_amount = remaining_amount + total_spent  # initial amount in savings account
    result = initial_amount
    return result

print(solution())